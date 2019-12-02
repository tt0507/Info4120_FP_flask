from twilio.rest import Client

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Please answer the survey http://127.0.0.1:5000/survey",
                     from_='+19739754465',
                     to='+16072795940'
                 )

print(message.sid)