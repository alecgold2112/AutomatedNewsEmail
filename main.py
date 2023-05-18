import requests
from send_email import send_email

topic = "tesla"

api_key = "7f82b7e5f1de4cddb421e1a99dc146f2"

# You can change 'tesla' to any topic
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-04-18" \
      "&sortBy=publishedAt&" \
      "apiKey=7f82b7e5f1de4cddb421e1a99dc146f2&" \
      "language=en"

# Make Request
req = requests.get(url)

# Get a dictionary with data
content = req.json()

# Access article titles and descriptions
body = ""
for article in content["articles"][:20]:
      body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" + article["description"] + \
             "\n" + article["url"] + 2*"\n"


body = body.encode("utf-8")
send_email(message=body)