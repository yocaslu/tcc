from flask import Flask, send_file

app = Flask(__name__)

REMOTE_CONTROL_API_KEY = 'aa13c710bab642ca843ef59595d6341' 

@app.route("/compliments.json")
def compliments():

    data = {"anytime": "Hey test from Python!"}
    # data = {
    #     "anytime": ["Hey there sexy!"],
    #     "morning": [
    #         "Good morning, sunshine!",
    #         "Who needs coffee when you have your smile?",
    #         "Go get 'em, Tiger!"
    #     ],
    #     "afternoon": [
    #         "Hitting your stride!",
    #         "You are making a difference!",
    #         "You're more fun than bubble wrap!"
    #     ],
    #     "evening": [
    #         "You made someone smile today, I know it.",
    #         "You are making a difference.",
    #         "The day was better for your efforts."
    #     ]
    # }
    return send_file('compliments.json', mimetype='application/json') 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)