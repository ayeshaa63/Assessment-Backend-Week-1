"""This file defines the API routes."""

# pylint: disable = no-name-in-module

from datetime import datetime

from flask import Flask, Response, request, jsonify

from date_functions import convert_to_datetime, get_day_of_week_on, get_days_between

app_history = []

app = Flask(__name__)


def add_to_history(current_request):
    """Adds a route to the app history."""
    app_history.append({
        "method": current_request.method,
        "at": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "route": current_request.endpoint
    })


@app.get("/")
def index() -> Response:
    """Returns an API welcome message."""
    return jsonify({"message": "Welcome to the Days API."})


@app.post("/between")
def between() -> Response:
    '''Returns the number of days between the dates given'''
    add_to_history(request)

    data = request.json

    if not all([k in data for k in ['first', 'last']]):
        return {"error": "Missing required data."}, 400

    try:
        date1 = convert_to_datetime(data['first'])
        date2 = convert_to_datetime(data['last'])
        days_between = get_days_between(date1, date2)

        return {'days': days_between}, 200

    except:
        return {"error": "Unable to convert value to datetime."}, 400


@app.post("/weekday")
def weekday() -> Response:
    '''Returns the weekday a particular date falls on'''
    add_to_history(request)

    data = request.json

    if not "date" in data:
        return {"error": "Missing required data."}, 400

    try:
        date1 = convert_to_datetime(data['date'])
        d_o_w = get_day_of_week_on(date1)
        return {'weekday': d_o_w}
    except:
        return {"error": "Unable to convert value to datetime."}, 400


@app.route("/history", methods=["GET", "DELETE"])
def history() -> Response:
    '''Displays history starting from most recent or clears history'''
    add_to_history(request)

    if request.method == 'GET':

        args = request.args.to_dict()
        number = args.get('number')

        if not number:
            number = 5

        try:
            number = int(number)
            if not 0 < number <= 20:
                raise ValueError()
        except:
            return {"error": "Number must be an integer between 1 and 20."}, 400

        print(app_history)
        return app_history[-1: -number - 1: -1], 200

    if request.method == 'DELETE':

        app_history.clear()

        return {"status": "History cleared"}, 200


if __name__ == "__main__":
    app.run(port=8080, debug=True)
