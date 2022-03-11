# Flask applications are all about requests and responses. We receive
# a request from a client, and it is the Flask server's job to 
# process the request and send a response.

from flask import Flask

# flask is the module, and Flask is the class. Modules begin with a lower
# case letter, whereas classes begin with an upper case.

app = Flask(__name__)

# __name__ is the name of this file

@app.route("/")    # e.g. "http://www.google.com/ - homepage
def home():
    # This method must return a response - this is what you see in your browswer
    return "Hello world!"

app.run(port=5000)
# If you then access this port on your computer's IP address in a browser
# you will see the "Hello world!" response