from twilio.rest import Client


account_sid = 'AC9ecc9fc2e6eb35838aeeb9cf89e203cd'
auth_token = '46cabc7d8bf35f7b0ccdb1ae0ce1d708'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Please answer the survey http://127.0.0.1:5000/survey",
                     from_='+19739754465',
                     to='+16072795940'
                 )

print(message.sid)