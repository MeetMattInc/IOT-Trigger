# iot_trigger.py - Simple script used to tirgger the Meet Matt IOT trigger
# located on the Zapier platform. Data should be formatted in JSON format and
# sent to the webhook provided.

import requests

webhook = 'https://hooks.zapier.com/hooks/catch/1511462/mrw9se/'
# static_hook = 'https://hooks.zapier.com/hooks/catch/1511462/mc3eag/'
marc = {
        "weight": "140",
        "date_time": "2017-02-05 16:06:24",
        "user_id": "Marc"
}

lucas = {
        "weight": "175",
        "date_time": "2017-02-05 16:06:24",
        "user_id": "Lucas"
}

tian = {
        "weight": "160",
        "date_time": "2017-02-05 16:06:24",
        "user_id": "Tian"
}

anthony = {
        "weight": "180",
        "date_time": "2017-02-05 16:06:24",
        "user_id": "Anthony"
}

profile = [marc, lucas, anthony, tian]

for user in profile:
    response = requests.post(webhook, json=user)
    while response.status_code != 200:
        continue

print('Done')
