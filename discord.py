import scrapper
import requests

webhook = 'https://discord.com/api/webhooks/1112508094178672751/h7GmhOUEESVxA4mB61o0JR4lKLPajsDlCFIzAjOmrIvn8KJ_Kvo7P1AKiInCSh2D25Lj'


def post(ad: scrapper.Ad) -> None:
    image = 'https://www.fishfish.fr/check/image?url=https%253A%252F%252Fzupimages.net%252Fviewer.php%253Fid%253D23%252F13%252Fv5mo.jpg'

    if len(ad.images) > 0:
        image = ad.images[0]
    message = {
        'content': '<@&1113840586429042840>',
        'embeds': [
            {
                'title': f'**{ad.price}€**・{ad.title}',
                'description': ad.url,
                'image': {'url': image},
                'footer': {
                    'text': f'{ad.account.username}',
                    'icon_url': ad.account.profile_picture
                }
            }
        ]
    }
    return requests.post(webhook, json=message)
