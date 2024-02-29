
# import smtplib
# from email.mime.text import MIMEText
# subject = "Email Subject"
# body = "This is the body of the text message tinubu funniest quote will be broom brooooooom broooooooooooo"
# sender = "danoritic@lifeclip.netlify.app"
# recipients = ["danoritic@gmail.com"]
# password = "$Dan0r1t1c$"


# def send_email(subject, body, sender, recipients, password):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = sender
#     msg['To'] = ', '.join(recipients)
#         # 465
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
#        smtp_server.login(sender, password)
#        smtp_server.sendmail(sender, recipients, msg.as_string())
#     print("Message sent!")


# if __name__=="__main__":
#     send_email(subject, body, sender, recipients, password)


# import base64
# from email.message import EmailMessage

# import google.auth
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError


# def gmail_create_draft():
#   """Create and insert a draft email.
#    Print the returned draft's message and id.
#    Returns: Draft object, including draft id and message meta data.

#   Load pre-authorized user credentials from the environment.
#   TODO(developer) - See https://developers.google.com/identity
#   for guides on implementing OAuth2 for the application.
#   """
#   creds, _ = google.auth.default()

#   try:
#     # create gmail api client
#     service = build("gmail", "v1", credentials=creds)

#     message = EmailMessage()

#     message.set_content("This is automated draft mail")

#     # message["To"] = "gmail@workspacesamples.dev"
    
#     # message["From"] = "gduser2@workspacesamples.dev"
#     # message["Subject"] = "Automated draft"

#     message["To"] = "danoritic@gmail.com"
    
#     message["From"] = "danoritic2@gmail.com"
#     message["Subject"] = "Automated draft   TINUBU BE THE PRESIDO "


#     # encoded message
#     encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

#     create_message = {"message": {"raw": encoded_message}}
#     # pylint: disable=E1101
#     draft = (
#         service.users()
#         .drafts()
#         .create(userId="me", body=create_message)
#         .execute()
#     )

#     print(f'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')

#   except HttpError as error:
#     print(f"An error occurred: {error}")
#     draft = None

#   return draft


# if __name__ == "__main__":
#   gmail_create_draft()


import base64
from email.message import EmailMessage
import json

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials



def gmail_send_message():
  """Create and send an email message
  Print the returned  message id
  Returns: Message object, including message id

  Load pre-authorized user credentials from the environment.
  TOcreds, _ = google.auth.default()
    DO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """
  
  credentialInDictFormat={}
  with open('email_sending_credentials.json','r') as f:
      credentialInDictFormat=json.loads(f.read())
  
  print(type(credentialInDictFormat))
  creds, _ = google.auth.load_credentials_from_dict({})
  print(creds)
  print('2'*50)
  print(_)
  print('2'*50)
  try:
    service = build("gmail", "v1", credentials=creds)
    message = EmailMessage()

    message.set_content("   TINUBU BE THE PRESIDO ooo"* 20)

    message["To"] = "danoritic@gmail.com"
    message["From"] = "danoritic2@gmail.com"
    message["Subject"] = "WHO BE THE PRESIDENT"
#     message["To"] = "danoritic@gmail.com"
    
#     message["From"] = "danoritic2@gmail.com"
#     message["Subject"] = "Automated draft   TINUBU BE THE PRESIDO "
    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {"raw": encoded_message}
    # pylint: disable=E1101
    send_message = (
        service.users()
        .messages()
        .send(userId="me", body=create_message)
        .execute()
    )
    print(f'Message Id: {send_message["id"]}')
  except HttpError as error:
    print(f"An error occurred: {error}")
    send_message = None
  return send_message


if __name__ == "__main__":
  gmail_send_message()