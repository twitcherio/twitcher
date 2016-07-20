#render template so that we can use the template
#templates directory is for HTML files that you can plug data into
#static directory is for things that dont change like the css file
from flask import Flask, render_template, request
#import BaseConverter
from werkzeug import routing


#instilize the flask application
app = Flask(__name__, static_url_path="", static_folder="static")

class RegexConvertor(routing.BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConvertor, self).__init__(url_map)
        self.regex = items[0]

#use the RegexConvertor function as a converter
#method for mapped urls
app.url_map.converters['regex'] = RegexConvertor

#this route will show some links matching(or not)
#the regex that we are setting on the next route
@app.route('/<regex("[abcABC0-9]{4,6}"):uid>-<slug>/')
def example(uid, slug):
    return "uid: %s, slug: %s" % (uid, slug)


@app.route('/')
def index():
    #whenever this URL is reached, the program is going to look for a file called homepage.html
    #filter will be the inputted name
    #whatever return value you have is basically the response of the server so you can put HTML directly in it
    #you almost never want to put HTML in this file
    return render_template("homepage.html")

    ##return 'Method used %s' % request.method



@app.route('/<handle>/<filter>')
def filters(handle, filter=None):

    # import twython
    from twython import Twython
    # import simplejson
    import simplejson
    # import RegEx (only find all function)
    from re import findall
    # import RegEx(find)
    import re

    # pip install twython
    # Requires Authentication as of Twitter API v1.1
    t = Twython(app_key='z8eLwuxMOedusXmzOHvFIQX0o',  # REPLACE 'APP_KEY' WITH YOUR APP KEY, ETC., IN THE NEXT 4 LINES
                app_secret='3KF164w8GLG7Tg6Nb5czMmCE2j54uOuS6GvNMM4130FYJXiVc7',
                oauth_token='752567920316837888-T5se5iPGLJbLcS4Jnfh1q4tNBHpK3My',
                oauth_token_secret='oXejT8THNR33ziZMhRSpWdPAgC4xEh4HxKBtzE5cOU2my')

    # allows user input for twitter handle (-@)
    twitter_handle = handle

    # get the user's tweets including retweets
    user_tweets = t.get_user_timeline(screen_name=twitter_handle, use_expanded_url=True, include_rts=True, count=200)

    # parse 200 tweets
    # next time you call the API set max ID to last twitter ID you


    # write the list of dictionaries into a .txt file
    #f = open('output.txt', 'w')
    #simplejson.dump(user_tweets, f)
    #f.close()

    # read in the .txt file into a string
    #f = open('output.txt', 'r')
    #all_lines = f.read()
    #f.close()
    ##print("File contents: ", all_lines)
    all_lines = str(user_tweets)
    #all_lines = "Bernie wall terrorism buckets popcorn vmware muslim"

    # make the search term input = profanity and then it searches those words
    search = filter

    # if they search the word profanity, it will filter the text to find these words
    if search == "profanity":
        # RegEx to search the .txt file for keywords
        regex = "'text': '([^']*( shit | fuck | damn | bitch | ass )[^']*)'"

        dataCrop = findall(regex, all_lines)

    # if they search the string 'nice things', then it will filter the text to find the word love
    if search == "nice things":
        regex = "'text': '([^']*( love | volunteering | donation | donate | charity | award | happiness | gratitude | success )[^']*)'"

        dataCrop = findall(regex, all_lines)


    # if they search 'drugs', then it will show up with anything to do with 421, etc.
    if search == "drugs":
        regex = "'text': '([^']*( marijuana | coccaine | weed | 420 | crack | blazin | heroin | joint | cannabis | hash | hemp | dope | drug | pot )[^']*)'"

        dataCrop = findall(regex, all_lines)


    # if they search the string 'alcohol', then it will filter the text to find alcohol
    if search == "alcohol":
        regex = "'text': '([^']*( shots | party | beer )[^']*)'"

        dataCrop = findall(regex, all_lines)


    # if they search the string 'school', then it will filter the text to find things to do with college
    if search == "school":
        regex = "'text': '([^']*( school | AP | honors | class )[^']*)'"

        dataCrop = findall(regex, all_lines)


    # if they search the string 'politics', then it will filter the text to find donald trump's offensive shit
    if search == "politics":
        regex = "'text': '([^']*( hispanics | Republican | Democrat | Hillary | Trump | Bernie | wall | immigration | alien | gun | Muslim | terrorist )[^']*)'"

        dataCrop = findall(regex, all_lines)

    # if they search the string 'coding', then it will filter the text to find things to do with coding
    if search == "coding":
        regex = "'text': '([^']*( code | coding | Python | Java | tech | programming | robotic | hack| software | API | JavaScript )[^']*)'"

        dataCrop = findall(regex, all_lines)

    # if they search the string 'employment', then it will filter the text to find things to do with the workplace
    if search == "employment":
        regex = "'text': '([^']*( job | boss | worker | work | internship )[^']*)'"

        dataCrop = findall(regex, all_lines)

    ### if they search the string 'school', then it will filter the text to find things to do with college
    ##if search == "employment":
        ##regex = "'text': '([^']*( job | boss | worker | work | internship )[^']*)'"

        ##dataCrop = findall(regex, all_lines)
        #dataCrop = findall("Bernie", all_lines)
        print("datacrop")
        #print(dataCrop)


    #tweets = dataCrop
    listlength = len(dataCrop)


    for x in dataCrop:
        print(x)

    if dataCrop == []:
        dataCrop = [("This filter returned no flagged tweets from this user.", "")]

    words = "("
    data = str(dataCrop)
    count = data.count(words)
    return render_template("filters.html", tweets=dataCrop, filter=filter, count=count, handle=handle)


    #return render_template(handle + " has been flagged " + str(count) + " time(s) for " + filter)

#this regex will match any combination of letters and numbers between 4 and 6 characters, followed by a - and a slug,
#a text string the first part will get the identifier "uid", while the slug is going to be called slug
#both parameters are passed to the view, that will print both values to prove they are correct


if __name__ == '__main__':
    app.run()