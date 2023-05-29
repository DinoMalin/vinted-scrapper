import scrapper
import discord

items = [scrapper.Item('Chemise', ['chemise'], (20, 30))]

for item in items:
    ads = scrapper.scrap(item, (0, 1))
    for ad in ads:
        print(ad.id)
        discord.post(ad)
