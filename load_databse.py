from database import DatabaseManger
from requests_api import RequestApi
from algorithm.algo import algo
import json


if __name__ == '__main__':
    ra = RequestApi()
    with DatabaseManger() as db:
        db.create_database()
        for date_key, data in ra.get_dates_data():
            windows = data['windows']['data']
            windows_for_room = data['windows_for_room']['data']
            api_check = ra.check_api(date_key, algo(windows, windows_for_room))
            db.insert_date(date_key, json.dumps(windows), json.dumps(windows_for_room), api_check)





