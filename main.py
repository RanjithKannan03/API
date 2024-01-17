import io

import requests
from PIL import Image

API_KEY="live_5Jo8nnq6VmN2tGn7Iq3MGHAvoMmQZuBP2WJ1oPVTVhYc2nWW2SQ5lpeBfJtcLlWu"

header={
'x-api-key' : API_KEY
}

params={
    'limit':100
}

response=requests.get("https://api.thecatapi.com/v1/images/search",headers=header,params=params)

cats=response.json()
i=1
for cat in cats:
    response=requests.get(cat['url'])
    image=Image.open(io.BytesIO(response.content))
    image.save(f'cats/{i}.png')
    i+=1
