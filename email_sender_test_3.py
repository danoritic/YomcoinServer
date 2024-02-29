import requests


def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxed87489396db44eeb9e8420750b34366.mailgun.org/messages",
        auth=("api", "df7e9f93af2804a07e337c74b8c3b4a6-4c955d28-02e0b531"),
        # https://app.mailgun.com/app/sending/domains/sandboxed87489396db44eeb9e8420750b34366.mailgun.org
        data={
          # "from": "Excited User <mailgun@YOUR_DOMAIN_NAME>",
          #     "to": ["bar@example.com", "YOU@YOUR_DOMAIN_NAME"],
          "from": "Excited User <mailgun@sandboxed87489396db44eeb9e8420750b34366.mailgun.org>",
              "to": ["danoritic@gmail.com", "danoritic2@gmail.com"],
          
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})

if __name__ == "__main__":
  d=send_simple_message()
  print(d.json())
