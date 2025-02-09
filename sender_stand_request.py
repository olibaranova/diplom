import requests
import configuration
import data

def new_order(body):
    response_order = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)
    return response_order

def get_new_track(track):  
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK + str(track))
    return get_new_track
 