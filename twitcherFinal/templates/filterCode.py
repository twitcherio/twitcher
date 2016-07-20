# This file is written for Python 3

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
twitter_handle = input("Enter twitter user: ")

# get the user's tweets including retweets
user_tweets = t.get_user_timeline(screen_name=twitter_handle, include_rts=True, count=200)

# parse 200 tweets
# next time you call the API set max ID to last twitter ID you


# write the list of dictionaries into a .txt file
f = open('output.txt', 'w')
simplejson.dump(user_tweets, f)
f.close()

# read in the .txt file into a string
f = open('output.txt', 'r')
all_lines = f.read()
f.close()
##print("File contents: ", all_lines)

# now we can see that the list of dictionaries is a string
##print(type(all_lines))

# make the search term input = profanity and then it searches those words
search = input("Enter search group('profanity', 'drugs', 'alcohol', 'nice things' or 'school'): ")

# if they search the word profanity, it will filter the text to find these words
if search == "profanity":
    # RegEx to search the .txt file for keywords
    regex = '"text": "([^"]*(shit|fuck|damn|bitch|ass)[^"]*)'

    dataCrop = findall(regex, all_lines)
    print(dataCrop)

# if they search the string 'nice things', then it will filter the text to find the word love
if search == "nice things":
    regex = '"text": "([^"]*(love|volunteering|donation|donate|charity|award)[^"]*)'

    dataCrop = findall(regex, all_lines)
    print(dataCrop)

# if they search 'drugs', then it will show up with anything to do with 421, etc.
if search == "drugs":
    regex = '"text": "([^"]*(marijuana|coccaine|weed|420|crack|blazin|heroin|high|joint|cannabis|hash|hemp|dope|drug|pot)[^"]*)'

    dataCrop = findall(regex, all_lines)
    print(dataCrop)

# if they search the string 'alcohol', then it will filter the text to find alcohol
if search == "alcohol":
    regex = '"text": "([^"]*(shots|party|beer)[^"]*)'

    dataCrop = findall(regex, all_lines)
    print(dataCrop)

# if they search the string 'school', then it will filter the text to find things to do with college
if search == "school":
    regex = '"text": "([^"]*(school|ap|honors|class)[^"]*)'

    dataCrop = findall(regex, all_lines)
    print(dataCrop)

# if they search the string 'politics', then it will filter the text to find donald trump's offensive shit
if search == "politics":
    regex = '"text": "([^"]*(hispanics|republican|Hillary|Bernie|wall|immigration|alien|gun|muslim|terrorist)[^"]*)'

    dataCrop = findall(regex, all_lines)
    print(dataCrop)