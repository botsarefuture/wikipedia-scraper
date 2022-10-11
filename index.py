
import requests
import time
READY = []
CONS = []
LANG = "fi"
FROM = "A"
TO = "Ö"
f = open("datas.txt", "r")
data = f.read()
f.close()
data = data.split("\n")
for data in data:
    READY.append(data)
def start(READY, request, cont):
    response = request()
    f = open("datas.txt", "a")
    for cat in response.json()["query"]["allpages"]:
        f.write(cat["title"] + "\n")
        READY.append(cat["title"])
        print(cat["title"])
    f.close()
    cont(response)

try:
    def request():
        try:
            url = f"https://{LANG}.wikipedia.org/w/api.php?action=query&list=allpages&apfrom={FROM}&apto={TO}&format=json&aplimit=20"

            payload={}
            headers = {
        'Cookie': 'GeoIP=US:VA:Ashburn:39.05:-77.49:v4; WMF-Last-Access-Global=10-Oct-2022; WMF-Last-Access=10-Oct-2022'
        }

            response = requests.request("GET", url, headers=headers, data=payload)
            return response
        except UnicodeDecodeError:
            print("Unicode")
            return request()
    def req_continue(con_ey):
        try:
            if not con_ey in CONS:
                CONS.append(con_ey)
                url = f"https://{LANG}.wikipedia.org/w/api.php?action=query&list=allpages&apfrom={FROM}&apto={TO}&format=json&apcontinue={con_ey}&aplimit=1000000"

                payload={}
                headers = {
            'Cookie': 'GeoIP=US:VA:Ashburn:39.05:-77.49:v4; WMF-Last-Access-Global=10-Oct-2022; WMF-Last-Access=10-Oct-2022'
            }

                response = requests.request("GET", url, headers=headers, data=payload)
                f = open("cat.txt", "w")
                f.write(response.json()["continue"]["apcontinue"])
                f.close()
                print("GETTED DATA")
                time.sleep(2)
                return response
            return request()
        except UnicodeDecodeError:
            print("UNi")
            return request()
    def cont(response):
        if type(response) == str:
            try:
                response = req_continue(response)
                datas_add = """"""
                
                for cat in response.json()["query"]["allpages"]:
                    if not cat["title"] in READY:
                        datas_add += cat["title"] + "\n"
                        READY.append(cat["title"])
                        print("ready")
                f = open("datas.txt", "a")
                f.write(datas_add)
                f.close()
                cont(response)
            except UnicodeEncodeError:
                print("UNICODE")
                cont(response)
        else:
            try:
                response = req_continue(response.json()["continue"]["apcontinue"])
                datas_add = """"""
                for cat in response.json()["query"]["allpages"]:
                    if not cat["title"] in READY:
                        datas_add += cat["title"] + "\n"
                        READY.append(cat["title"])
                        print(cat["title"])
                f = open("datas.txt", "a")
                f.write(datas_add)
                f.close()
                cont(response)
            except UnicodeEncodeError:
                print("UNICODE")
                cont(response)

    start(READY, request, cont)
except RecursionError:
    print("recursion")
    start(READY, request, cont)
except UnicodeEncodeError:
    print("unicode")
    start(READY, request, cont)
