__author__ = 'Tim'

from flask import Flask, request, render_template
import twilio.twiml
from application import app

callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
    "+15714470280": "Tim",
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():

    from_number = request.values.get('From', None)
    if from_number in callers:
        caller = callers[from_number]
    else:
        caller = "Monkey"

    resp = twilio.twiml.Response()

    resp.say("Hello " + caller)

    resp.play("http://demo.twilio.com/hellomonkey/monkey.mp3")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)