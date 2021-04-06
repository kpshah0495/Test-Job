import sys
import os
import requests
import json

data={
    "fields": {
        "[Confirmation] Posted on Hirist": True
        },
    "typecast": True
    }

header= {"Authorization": "Bearer " + "keynRNfKupAXaHbAO"}

response = requests.patch("https://api.airtable.com/v0/appvAQN63wuB48KmW/High%20Priority%20Positions/recedmuY36R3wXZht", headers=header,json=data)
r = response.json()

