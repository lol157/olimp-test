import requests


class RequestApi:
    @staticmethod
    def get_date(date):
        day, month, year = date.split('-')
        return requests.get(f"http://26.241.32.104:5001/?day={day}&month={month}&year={year}").json()['message']

    def get_dates_data(self):
        dates = requests.get(f"http://26.241.32.104:5001/date").json()['message']

        return [(date, self.get_date(date)) for date in dates]

    @staticmethod
    def check_api(date_key, algo_answer):
        j = {
            "data": {
                "count": len(algo_answer),
                "rooms": algo_answer
            },
            "date": date_key
        }

        return requests.post('http://26.241.32.104:5001/', json=j).json()['message']



