from flask import Flask, request, jsonify
from flask_cors import CORS
from blackjack import BlackJack
from edible import Edible

app = Flask(__name__)
CORS(app)
bj = None
food_game = None


@app.route("/blackjack", methods=["GET", "POST"])
def blackjack():
    global bj
    req = request.get_json()

    response = {
        "version": req["version"],
        "session": req["session"],
        "response": {
            "text": "Не знаю такой команды",
            "end_session": False,
        }
    }

    command = req["request"]["command"]

    if "старт" in command:
        bj = BlackJack()
        response["response"]["text"] = f"Ну давай-давай, нападай. Твой счёт {bj.human.score}"
        response["response"]["tts"] = f"Ну давай-давай, нападай. Твой счёт {bj.human.score}"
        response["response"]["buttons"] = [
            {
                "title": "Ещё",
                "url": "http://localhost:5000/blackjack"
            },
            {
                "title": "Хватит",
                "url": "http://localhost:5000/blackjack"
            }
        ]
        return jsonify(response)

    if bj:
        state, msg = bj.step(command)

        if not state:
            response["response"]["text"] = msg
            response["response"]["tts"] = msg
            response["response"]["buttons"] = [
                {
                    "title": "Ещё",
                    "url": "http://localhost:5000/blackjack"
                },
                {
                    "title": "Хватит",
                    "url": "http://localhost:5000/blackjack"
                }
            ]
            return jsonify(response)
        else:
            response["response"]["end_session"] = True
            response["response"]["text"] = msg
            response["response"]["tts"] = msg
            return jsonify(response)


@app.route("/edible", methods=["GET", "POST"])
def edible():
    global food_game
    req = request.get_json()

    response = {
        "version": req["version"],
        "session": req["session"],
        "response": {
            "text": "Не знаю такой команды",
            "end_session": False,
        }
    }

    command = req["request"]["command"]

    if "старт" in command:
        food_game = Edible()
        food, not_food = food_game.get_choices()
        response["response"]["text"] = f"Что же ты выберешь, смертный? \n Цель: {food_game.streak} / 20"
        response["response"]["tts"] = f"Что же ты выберешь, смертный? \n Цель: {food_game.streak} / 20"
        response["response"]["buttons"] = [
            {
                "title": food,
                "url": "http://localhost:5000/edible"
            },
            {
                "title": not_food,
                "url": "http://localhost:5000/edible"
            }
        ]

    if food_game:
        food_game.check(command)

        if food_game.streak == 10:
            response["response"]["text"] = "А ты хорош"
            response["response"]["tts"] = "А ты хорош"
            food_game = None
            return jsonify(response)

        food, not_food = food_game.get_choices()

        response["response"]["text"] = f"Что же ты выберешь, смертный? \n Цель: {food_game.streak} / 10"
        response["response"]["tts"] = f"Что же ты выберешь, смертный? \n Цель: {food_game.streak} / 10"
        response["response"]["buttons"] = [
            {
                "title": food,
                "url": "http://localhost:5000/edible"
            },
            {
                "title": not_food,
                "url": "http://localhost:5000/edible"
            }
        ]

    return jsonify(response)


@app.route("/tetris", methods=["GET", "POST"])
def tetris():
    pass


@app.route("/snake", methods=["GET", "POST"])
def snake():
    pass


@app.route("/binary", methods=["GET", "POST"])
def binary():
    pass


if __name__ == '__main__':
    app.run(debug=True)
