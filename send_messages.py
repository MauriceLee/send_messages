from twilio.rest import Client

account_sid = "AC848589c347e20d13753324b4c13fb91e"

auth_token = "a1a215247fd5b7083c591b114a886063"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to = "+886XXXXXXXXX",
    from_ = "+16677714315",
    body = "我不用手機就可以傳簡訊給我的愛人耶")

print(message.sid)