from json import dumps
from flask import Flask, request
from flask_cors import CORS
from suburbs import get_suburbs
from crashcount import getAllCrashesOnRoute
from traffic_data import getAllTrafficOnRoute

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
    #data = request.get_json()
    data = {}
    data['source'] = '29 Riverview Rd, Pleasure Point NSW 2172'
    data['destination'] = 'Zeus Street Greek Broadway Sydney, 1-21 Bay Street Level 2, Broadway, NSW 2007'
    suburb_data = get_suburbs(str(data['source']), str(data['destination']))
    # call crashcount here
    information = []
    for route in suburb_data:
        information.append({})
    
    '''
    [
        {
            'crashes'
            'traffic'
        }
    ]
    '''
    for index, route in enumerate(suburb_data):
        information[index]['crashes'] = getAllCrashesOnRoute(route)
        information[index]['traffic'] = getAllTrafficOnRoute(route)
    print(information)
    returned = []
    for route in information:
        calculation = (route['crashes'] * 100000000000000)/route['traffic']
        returned.append(calculation)
    # change this return value
    return dumps(returned)

    
if __name__ == "__main__":
    APP.run(port=0) # Do not edit this port