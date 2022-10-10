
import requests
READY = []
CONS = []
try:
    def request():
        url = "https://fi.wikipedia.org/w/api.php?action=query&list=allpages&apfrom=B&format=json"

        payload={}
        headers = {
    'Cookie': 'GeoIP=US:VA:Ashburn:39.05:-77.49:v4; WMF-Last-Access-Global=10-Oct-2022; WMF-Last-Access=10-Oct-2022'
    }

        response = requests.request("GET", url, headers=headers, data=payload)
        return response
    def req_continue(con_ey):
        if not con_ey in CONS:
            CONS.append(con_ey)
            url = f"https://fi.wikipedia.org/w/api.php?action=query&list=allpages&apfrom=B&format=json&apcontinue={con_ey}"

            payload={}
            headers = {
        'Cookie': 'GeoIP=US:VA:Ashburn:39.05:-77.49:v4; WMF-Last-Access-Global=10-Oct-2022; WMF-Last-Access=10-Oct-2022'
        }

            response = requests.request("GET", url, headers=headers, data=payload)
            return response
        return request()
    def cont(response):
        try:
            response = req_continue(response.json()["continue"]["apcontinue"])
            f = open("datas.txt", "a")
            for cat in response.json()["query"]["allpages"]:
                if not cat["title"] in READY:
                    f.write(cat["title"] + ",")
                    READY.append(cat["title"])
                    print(cat["title"])
                else:
                    print("LOOPING WARNING")
            f.close()
            cont(response)
        except UnicodeEncodeError:
            print("UNICODE")
            print(response.text)
            cont(response)

    response = request()
    f = open("datas.txt", "a")
    for cat in response.json()["query"]["allpages"]:
        f.write(cat["title"] + ",")
        READY.append(cat["title"])
        print(cat["title"])
    f.close()
    cont(response)
except RecursionError:
    def request():
        url = "https://fi.wikipedia.org/w/api.php?action=query&list=allpages&apfrom=B&format=json"

        payload={}
        headers = {
    'Cookie': 'GeoIP=US:VA:Ashburn:39.05:-77.49:v4; WMF-Last-Access-Global=10-Oct-2022; WMF-Last-Access=10-Oct-2022'
    }

        response = requests.request("GET", url, headers=headers, data=payload)
        return response
    def req_continue(con_ey):
        if not con_ey in CONS:
            CONS.append(con_ey)
            url = f"https://fi.wikipedia.org/w/api.php?action=query&list=allpages&apfrom=B&format=json&apcontinue={con_ey}"

            payload={}
            headers = {
        'Cookie': 'GeoIP=US:VA:Ashburn:39.05:-77.49:v4; WMF-Last-Access-Global=10-Oct-2022; WMF-Last-Access=10-Oct-2022'
        }

            response = requests.request("GET", url, headers=headers, data=payload)
            return response
        return request()
    def cont(response):
        try:
            response = req_continue(response.json()["continue"]["apcontinue"])
            f = open("datas.txt", "a")
            for cat in response.json()["query"]["allpages"]:
                if not cat["title"] in READY:
                    f.write(cat["title"] + ",")
                    READY.append(cat["title"])
                    print(cat["title"])
                else:
                    print("LOOPING WARNING")
            f.close()
            cont(response)
        except UnicodeEncodeError:
            print("UNICODE")
            print(response.text)
            cont(response)

    response = request()
    f = open("datas.txt", "a")
    for cat in response.json()["query"]["allpages"]:
        f.write(cat["title"] + ",")
        READY.append(cat["title"])
        print(cat["title"])
    f.close()
    cont(response)
