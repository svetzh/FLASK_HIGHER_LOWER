from flask import Flask
from random import randint


app = Flask(__name__)

@app.route("/")
def home():
    return ('''<div style="text-align: center;">
                <h1>Guess a number between 0 and 9</h1>
                <img src="https://media.giphy.com/media/7CkoBzGDF1cD6Wk54G/giphy.gif" alt="Random GIF">
            </div>''')

random_number = randint(0, 9)

@app.route("/<int:guess_num>")
def guess_number(guess_num):
    global random_number

    if guess_num > random_number:
        return ('''<div style="text-align: center;">
                <h1 style="color: purple">Too HIGH! Guess again!</h1>
                <img src="https://media.giphy.com/media/gBTA6sZZHmeF0Mrhm5/giphy.gif">
            </div>''')
    elif guess_num < random_number:
        return ('''<div style="text-align: center;">
                <h1 style="color: red">Too low! Guess again!</h1>
                <img src="https://media.giphy.com/media/YnNNtmpr9bZlEAdMKG/giphy.gif">
            </div>''')
    else:
        return ('<div style="text-align: center;">'
                f'<h1 style="color: green"><b>Correct: {guess_num}</b></h1>'
                '<img src="https://media.giphy.com/media/UXgf6pu1LlQp6CPDi0/giphy.gif">'
                '</div>'
                )


if __name__ == "__main__":
    app.run(debug=True)