from scrapper import scrap
from objects import Item
import discord
import db
import time
import random

items = [Item("Chemise", ["chemise"], (20, 30))]


def main():
    for item in items:
        ads = scrap(item, (0, 1))
        for ad in ads:
            if not db.exists(ad):
                response = discord.post(ad)
                print(ad.id)
                if response.status_code == 200:
                    db.save(ad)
                time.sleep(0.5)
            else:
                print("already exists")


while True:
    main()
    time.sleep(random.randint(60, 120))
# main()
