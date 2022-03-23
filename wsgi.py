import os
from flask import Flask, jsonify
HOST_NAME = os.environ.get('OPENSHIFT_APP_DNS', 'localhost')

application = Flask(__name__)

@application.route("/")
def hello():
    return jsonify({
        'host_name': HOST_NAME,
    })
    
    # return "Hello World!"

if __name__ == "__main__":
    application.run()
