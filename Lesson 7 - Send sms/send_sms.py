from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACacbecc3511b92bb37f085a3a4e7fe0a3"
auth_token = "9695de289b3e1b0751b76ee023d3df1a"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+393347979500",
    from_="+15005550006",
    body="Hello there! I'm Christopher! Nice to meet you!")

print(message.sid)
