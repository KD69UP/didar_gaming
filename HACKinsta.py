import cloudscraper as cs
from dhooks import Webhook, Embed
from time import sleep

scraper = cs.create_scraper()
webhook = Webhook("https://discord.com/api/webhooks/1088213603955507210/jxjjQ6ttsOuHNg8Pz_dw_-9fJCHdp8eXOTkwGv8iIhhlTp5qisMmgiUgeyEuWIQDjcxd")

while True:
    rain_active = False
    if rain_active == False:
        r = scraper.get("https://api.bloxflip.com/chat/history").json()['rain']
        if r['active'] == True:
            prize = r['prize']
            em = Embed(color=0x0025ff, timestamp='now')
            em.add_field(name='Rain!', value=f'Active Rain ${prize}[join rain](https://bloxflip.com)')
            em.set_timestamp
            webhook.send("@everyone")
            webhook.send(embed=em)
            rain_active = True
        else:
            rain_active = False
