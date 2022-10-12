
import requests
import time

READY = []
CONS = []
LANG = "fi"
FROM = "A"
TO = "Ö"
NUM_LIMIT = 5000
f = open("datas.txt", "r")
data = f.read()
f.close()
data = data.split("\n")
NUM_ITEMS = 0
for data in data:
    NUM_ITEMS += 1
    READY.append(data)
def count(lista):
    count1 = 0
    for list1 in lista:
        count1 += 1
    return count1
CON_KEY = ""
while True:
    try:
        if not CON_KEY == "":
            url = f"https://{LANG}.wikipedia.org/w/api.php?action=query&list=allpages&apfrom={FROM}&apto={TO}&format=json&apcontinue={CON_KEY}&aplimit={NUM_LIMIT}"

            payload={}
            headers = {
        'Cookie': 'GeoIP=US:VA:Ashburn:39.05:-77.49:v4; WMF-Last-Access-Global=10-Oct-2022; WMF-Last-Access=10-Oct-2022'
        }

            response = requests.request("GET", url, headers=headers, data=payload)
            CON_KEY = response.json()["continue"]["apcontinue"]
            #NUM_ITEMS += int(count(response.json()["query"]["allpages"]))
            print(f'GETTED {count(response.json()["query"]["allpages"])} ITEMS')
            print(f"TOTAL ITEMS COUNT: {NUM_ITEMS}")
            time.sleep(0.5)
            datas_add = """"""
            for cat in response.json()["query"]["allpages"]:
                if not cat["title"] in READY:
                    datas_add += cat["title"] + "\n"
                    READY.append(cat["title"])
                    NUM_ITEMS += 1
                    print(cat["title"])
            f = open("datas.txt", "a")
            f.write(datas_add)
            f.close()
        else:
            url = f"https://{LANG}.wikipedia.org/w/api.php?action=query&list=allpages&apfrom={FROM}&apto={TO}&format=json&aplimit={NUM_LIMIT}"
            payload={}
            headers = {
        'Cookie': 'GeoIP=US:VA:Ashburn:39.05:-77.49:v4; WMF-Last-Access-Global=10-Oct-2022; WMF-Last-Access=10-Oct-2022'
        }

            response = requests.request("GET", url, headers=headers, data=payload)
            CON_KEY = response.json()["continue"]["apcontinue"]
            #NUM_ITEMS += int(count(response.json()["query"]["allpages"]))
            print(f'GETTED {count(response.json()["query"]["allpages"])} ITEMS')
            print(f"TOTAL ITEMS COUNT: {NUM_ITEMS}")
            time.sleep(0.5)
            datas_add = """"""
            for cat in response.json()["query"]["allpages"]:
                if not cat["title"] in READY:
                    datas_add += cat["title"] + "\n"
                    READY.append(cat["title"])
                    NUM_ITEMS += 1
                    print(cat["title"])
            f = open("datas.txt", "a")
            f.write(datas_add)
            f.close()
    except UnicodeDecodeError:
        print("UNi")
    except UnicodeEncodeError:
        print("UNi")
