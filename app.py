import requests
import time
from bs4 import BeautifulSoup
import telegram

TOKEN = "8748197604:AAHsvqY0-TT0rUv01QFgj32xXmb0owfb0qg"
CHAT_ID = "65941056"

URL = "https://official-tickets.roadtoqat ar.qa/qatar-football"

bot = telegram.Bot(token=TOKEN)

def check_tickets():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    if "There are no tickets available" not in soup.text:
        bot.send_message(chat_id=CHAT_ID, text="🚨 Tickets are AVAILABLE! Check now!")
        print("Tickets found!")
    else:
        print("No tickets yet.")

while True:
    check_tickets()
    time.sleep(10)
