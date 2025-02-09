#Баранова_Ольга_26_когорта_диплом
from data import body
from sender_stand_request import new_order, get_new_track

def test_order():
    response_create = new_order(body)
    track = response_create.json()["track"]
    response_get = get_new_track(track)
    assert response_get.status_code == 200


