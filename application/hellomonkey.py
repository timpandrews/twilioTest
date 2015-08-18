__author__ = 'Tim'

from flask import Flask, request, render_template
import twilio.twiml
from twilio.rest import TwilioRestClient
from application import app

account_sid = "AC589a3ed91674960da23368d1d7562368"
auth_token = "4f6b68d5bacb7a5d354b6e8ce9b04891"
client = TwilioRestClient(account_sid, auth_token)

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
        from_num = from_number
    else:
        caller = "Monkey"
        from_num = "Unkown"

    print "From: ", from_num


    textTo = "+15714470280"
    textFrom = "+17039621286"
    textMsg = "Just recieved help phone call from " + from_num

    message = client.messages.create(to=textTo, from_=textFrom, body=textMsg)

    resp = twilio.twiml.Response()

    resp.say("Hello " + caller)

    resp.play("http://demo.twilio.com/hellomonkey/monkey.mp3")

    with resp.gather(numDigits=1, action="/handle-key", method="POST") as g:
        g.say("To speak to a real monkey, press 1.  Press any other key to start over.")

    return str(resp)

@app.route("/handle-key", methods=['GET', 'POST'])
def handle_key():
    """Handle key press from a user."""
 
    # Get the digit pressed by the user
    digit_pressed = request.values.get('Digits', None)
    if digit_pressed == "1":
        resp = twilio.twiml.Response()
        # Dial (310) 555-1212 - connect that number to the incoming caller.
        resp.dial("+7035730948")
        # If the dial fails:
        resp.say("The call failed, or the remote party hung up. Goodbye.")
 
        return str(resp)
 
    # If the caller pressed anything but 1, redirect them to the homepage.
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)