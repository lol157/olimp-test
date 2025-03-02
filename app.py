from flask import Flask, render_template, request
from database import DatabaseManger
from algorithm.algo import algo

app = Flask('__name__')


@app.route('/', methods=["GET"])
def home():
    return render_template('main.html')


@app.route('/dates', methods=["GET", "POST"])
def dates():
    with DatabaseManger() as db:
        if request.method == "POST":
            date = request.form['date']
            windows, windows_for_room, api_check = db.select_date(date)
            algo_res = algo(windows, windows_for_room)
            data = {"1": {"windows": [[[1, True], [1, True]], [[2, True], [3, False]]], "rooms_cnt": 6, "has_light": [3, 2, 4, 3], "is_correct": True},
                    "2": {"windows": [[[1, True], [1, True]], [[2, True], [3, False]]], "rooms_cnt": 6, "has_light": [3, 2, 4, 3], "is_correct": True},
                    "3": {"windows": [[[1, True], [1, True]], [[2, True], [3, False]]], "rooms_cnt": 6, "has_light": [3, 2, 4, 3], "is_correct": True},
            }

            if date == 'all_dates':
                return render_template('days.html', data=data)

            return render_template('days.html', data={date: data[date]})
        else:
            dates = ["1", '2', '3']
            return render_template('dates.html', dates=dates)


@app.route('/input', methods=["GET", "POST"])
def input():
    return render_template('input.html')


app.run(debug=True)