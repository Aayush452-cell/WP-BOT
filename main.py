from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def hello():
    return "HELLO WORLD"

@app.route('/sms',methods=['POST'])
def sms_reply():
    msg = request.form.get('Body')
    resp = MessagingResponse()
    resp.message("Hey {} I wish you a Nice Day ".format(msg))

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
