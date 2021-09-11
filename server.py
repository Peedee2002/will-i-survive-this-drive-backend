from json import dumps
from flask import Flask, request
from flask_cors import CORS
from suburbs import get_suburbs

def defaultHandler(err):
    response = err.get_response()
    print('response', err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response

APP = Flask(__name__)
CORS(APP)

APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)


# POST STUFF:
# JSON input 
# source : string
# destination : string
@APP.route("/suburbs", methods=['POST'])
def http_get_suburbs():
    data = request.get_json()
    suburb_data = get_suburbs(str(data['source']), str(data['destination']))
    # call crashcount here
    
    # change this return value
    return dumps(suburb_data)

    
if __name__ == "__main__":
    APP.run(port=0) # Do not edit this port