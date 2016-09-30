import credentials #credetials.py with the sid and token
from twilio.rest import TwilioRestClient

account_sid = credentials.twilio_sid # Your Account SID from www.twilio.com/console
auth_token  = credentials.twilio_auth_token  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello! Sent with Python",
    to="+40726752584",    # Replace with your phone number
    from_="+12018099932") # Replace with your Twilio number

print(message.sid)
