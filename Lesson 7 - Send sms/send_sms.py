from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACacbecc3511b92bb37f0***"
auth_token = "9695de289b3e1b0751***"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+393347979500",
    from_="+15005550006",
    body="Hello there! I'm Christopher! Nice to meet you!")

print(message.sid)
