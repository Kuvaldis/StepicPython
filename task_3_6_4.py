import requests
import json
import operator

client_id = 'bd1e33ea2438472c7706'
client_secret = '3c8a033eb39de67457a51535ca1d07b1'


def get_token():
    resp = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                         data={
                             "client_id": client_id,
                             "client_secret": client_secret
                         })
    j = json.loads(resp.text)
    return j["token"]


def get_artist_data(artist_id, token):
    headers = {"X-Xapp-Token": token}
    r = requests.get("https://api.artsy.net/api/artists/" + artist_id, headers=headers)
    j = json.loads(r.text)
    return (j['sortable_name'], j['birthday'])


token = get_token()
artist_ids = ['5324d4657622dd48700001e3',
 '4f552b2e3b55524170000003',
 '52699b14b202a3472d0002fc',
 '53330ad9cb4c27894a0000be',
 '4e2ed576477cc70001006f99',
 '519258cc9e628509c40000d7',
 '548632a7726169516a620100',
 '554a78d87261692b00710400',
 '554a788f726169251a210800',
 '4f552b2e3b55524170000002',
 '53e126267261692d6bf50100',
 '563c23147261693ed900068b',
 '52840714275b2442c8000150',
 '516df2b89ad2d38886001378',
 '4d8b92a44eb68a1b2c000328']
artists_data = [get_artist_data(artist_id, token) for artist_id in artist_ids]
print("\n".join(map(lambda x: x[0], sorted(artists_data, key=lambda x: (x[1], x[0])))))
