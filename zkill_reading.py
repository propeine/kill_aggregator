import requests
import json
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
plt.rcdefaults()


page_num = 1

# dictionary for how many pilots involved in killmails
pilots_involved = {
    "solo": 0,
    "five": 0,
    "ten": 0,
    "fifteen": 0,
    "twenty": 0,
    "thirty": 0,
    "forty": 0,
    "fifty": 0,
    "blob": 0,
}
char_id = input("Enter your character id from zkill: ")
# set up initial webpage hit
link = "https://zkillboard.com/api/kills/characterID/" + str(char_id) + "/no-attackers/page/" + \
    str(page_num) + "/"
response = requests.session()
response.headers.update(
    {'Accept-Encoding': 'gzip', "User-Agent": "Mozilla/5.0"})
response = requests.get(link)

# zkill returns [] if the page is empty
while response.text.find("[]") == -1:
    print("Reading page: " + str(page_num))
    cjson = json.loads(response.text)
    for i in range(len(cjson)):
        pilots = int(cjson[i]['zkb']['involved'])
        if int(pilots) == 1:
            pilots_involved["solo"] += 1
        elif int(pilots) < 5:
            pilots_involved["five"] += 1
        elif int(pilots) < 10:
            pilots_involved["ten"] += 1
        elif int(pilots) < 15:
            pilots_involved["fifteen"] += 1
        elif int(pilots) < 20:
            pilots_involved["twenty"] += 1
        elif int(pilots) < 30:
            pilots_involved["thirty"] += 1
        elif int(pilots) < 40:
            pilots_involved["forty"] += 1
        elif int(pilots) < 50:
            pilots_involved["fifty"] += 1
        elif int(pilots) >= 50:
            pilots_involved["blob"] += 1
    page_num += 1
    time.sleep(1.25)
    link = "https://zkillboard.com/api/kills/characterID/" + str(char_id) + "/no-attackers/page/" + \
        str(page_num) + "/"
    response = requests.get(link)

for x, y in pilots_involved.items():
    print(x + ": " + str(y))

pilots = pilots_involved.keys()
number = pilots_involved.values()
y_pos = np.arange(len(pilots))
plt.bar(pilots, number, align='center', alpha=0.5)
plt.ylabel('Number of Kills')
plt.title('Involved Pilots per KM')
plt.show()
