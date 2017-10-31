from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC81a56fd0a37f8dd042d31322fbd1f829"
# Your Auth Token from twilio.com/console
auth_token  = "7086d428e558f1afb1ac4f4385efc79e"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18646405680", 
    from_="+18646632052",
    body="This is fun! I'm sending text messages!")

print(message.sid)