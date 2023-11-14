import requests
from bs4 import BeautifulSoup
import json


saner = str(input("Bir kelime giriniz: "))

data = {
    "query_text_mf": saner,
    "query_text": saner
}

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "cookie": "SAHİBİNDEN SİTESİNE GİRİŞ YAPIP COOKİE'NİZİ YAZIN.",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

x = requests.get(f"https://www.sahibinden.com/vasita?pagingSize=50&query_text_mf={saner}&query_text={saner}", data=data, headers=headers)
y = BeautifulSoup(x.text, "html.parser")


sanersearchResultsRowClass = y.find_all(class_="searchResultsRowClass")

sanersayac = 0
data_list = []

for tr in sanersearchResultsRowClass:
    sanertr = tr.find_all("tr")
    for tr in sanertr:
        sanersayac = sanersayac + 1
        sanersearchResultsLargeThumbnail = sanertr[sanersayac-1]
        title_element = sanertr[sanersayac-1].find(class_="classifiedTitle")
        title = title_element.text.strip() if title_element else "Başlık Bulunamadı"

        image_element = sanertr[sanersayac-1].find("img")
        image_src = image_element["src"] if image_element else "Görsel Bulunamadı"

        store_element = sanertr[sanersayac-1].find(class_="titleIcon")
        store = store_element["title"] if store_element else "Mağaza Bulunamadı"

        price_element = sanertr[sanersayac-1].find(class_="classified-price-container")
        price = price_element.text.strip() if price_element else "Fiyat Bilgisi Bulunamadı"

        date_element = sanertr[sanersayac-1].find(class_="searchResultsDateValue")
        date = date_element.text.strip() if date_element else "Tarih Bilgisi Bulunamadı"

        location_element = sanertr[sanersayac-1].find(class_="searchResultsLocationValue")
        location = location_element.text.strip() if location_element else "Konum Bilgisi Bulunamadı"
        data_list.append({
            "title": title,
            "image_src": image_src,
            "store": store,
            "price": price,
            "date": date,
            "location": location
        })
        

z = y.find_all(class_="pageNaviButtons")

for button in z:
    li_elements = button.find_all("li")
    for li in li_elements:
        a_tag = li.find("a")
        if a_tag and a_tag.get("title") != "Sonraki":
            merhaba = "https://www.sahibinden.com"+a_tag.get("href")
            data = {
                "query_text_mf": saner,
                "query_text": saner
            }

            headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "cookie": "vid=773; cdid=xyh5wOHGkrEaDqmA65414688; csls=LLeuiViGZY7f5WHJU6D7AWZ2gvQQ73mJH_e0zuv3npbzjWsuNtH83cB-fttXS_Ue_hi6i7dbtf00f2YX4TRnptt3fP1k8S_T-Y9botBMLssXgec73AUlIpWZdpSOCrjeK5yPBWQou7Rc4N0BMHc7hEK1H5krWLmXoeNh4fGdBg8WR6IU_UyEQv1bs9VCRIQpAaB-1fohDhyDMk6MCu1S8hAdi1Q1NpdAj0hE13h0Ka0; nwsh=std; showPremiumBanner=false; MS1=https://www.google.com/; _gcl_au=1.1.1352070999.1698776715; __ssid=9865aeb351730ba0bb8601889883689; OptanonAlertBoxClosed=2023-10-31T18:25:22.571Z; _fbp=fb.1.1698776722642.1550116214; _gid=GA1.2.650369672.1699914396; st=a2a5341b399ad42fcaed481f616f8864f14edaf0f2193cba00578511defc0bf701989b719b425590c86aedb73262b542e2969f1db1fabe956; csss=FFX4ivQ642I6mVbnVp7V_QqBp_qnedG1ET8uQjd2nU7A8Gp1JTmnTEz9qSW3X_HuktL3GvayBwPnRXKnW2IoWzmeru-ZWMtBBU9_i_sGKBZD0FTcYWKMhCG5Qj4tWzXmxwK1HDU8goZcy1mIQY3ilv3ltrPJOozqNtL9vsraAwViIpJzH5kknhMBiScheCklVU_3sjVg9oan6R2LriFqxZmeCy86JfWkRZNoprjTCIA; __cf_bm=pSkzwq5_yjig8s4tAfV29T3TQC4QaL.bvxUtCVctuVg-1699992985-0-AUbF0AncjfQ4Vj86a96VGL8qDh0yaxamhiLJXt5H5Xv89ZSVI13VD35e01oyoivdUxc2ect21iSnqzA6HiEiGUU=; __cflb=0H28vudCb12J6LVB9qP4jWxLKyXe4Wk4yojqVYecfCX; dp=1920*1080-landscape; geoipCity=tekirdag; geoipIsp=turksat; __gads=ID=2924ba98445b1fc9:T=1698776714:RT=1699992986:S=ALNI_MYpt2rey_idElRHzlOBRK1YFauG3g; __gpi=UID=00000caf949993c2:T=1698776714:RT=1699992986:S=ALNI_MakKJA8Mj2JlDChrcM5gp3njYkMwQ; bannerClosed=false; searchType=TEXT/ENTER/CLASSIC; cf_clearance=2wTmT_flWpWb3XJSlOXtwCVFzUtRF6Z.ay__uiOe0Yc-1699993076-0-1-87a96194.4e73c24d.d0a83e74-250.2.1699992986; csid=4PkvJ7BM3a6jgjc24aCv7dKCplt1wzUGOcdJPDYmMlZ2zAmBoci8NhFbv7y22tKEziXIx9LHlsqw1hh--uk1BkjpZV0wKEzzrRj5yLyuupwAnPtUYglIzF2Fg1LAdqqG7hYvgR1kNGwYwoY70SB2AxMXmL0PwgMo2jrYJRwt_V9rgyXrMW67d8-QUjoF8k8fLunVTxqwaiDxWQ2ijF_X44d8t7vcFh5EIuUjwm_BZiUOcHvDfEuJojeOSLj9Xjt3RU6TAYs8GNoISIUsXydgYPWPjv5UXBJ47BatSQWMBZaNrTTNupJvZdxdXVXg4WKE-ghuKORiCydTSYhn-5gCp7b_089rMZN5iFNCeCn1rlk8sfuxLwYT5qyfEmHYVIDu3E89n4dRPVjjYessKiYH5Wv8k0vSWAc6ycHbYTdBqnzT21v1obb_09VIb_kr1wqllW_swSH53NCeiPOPBUUovsXiPN7dAwYqCc8UYlsxdEhQMu7FGmXb-vKZGqCmp-SK-HWh8MfO1jiVCvTQ7rnIltuJFfFFfF7UENnE-WNf_zeEpYwsq4EduiQLdKHGaeMOsemMDEW2yeHoUno0UuAu8dQrK4SKMQTklYVqcn9fbv8Wj-cQvLoxjlcsghvotg33_rQTTjU9f-MMpSi0lUU_7BRQhX3prQIrQKSWHTpSD5I; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Nov+14+2023+23%3A19%3A40+GMT%2B0300+(GMT%2B03%3A00)&version=6.22.0&isIABGlobal=false&hosts=&consentId=5c5e9df7-bb03-4d75-abbb-1ae2e0ddfddb&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=%3B&AwaitingReconsent=false; _ga_CVPS3GXE1Z=GS1.1.1699992988.3.1.1699993181.60.0.0; _ga=GA1.2.686423648.1698776715; _dc_gtm_UA-235070-1=1; cto_bundle=rJ3hjV9PT3ZxRFpGZDI2dXI0OUIlMkJTdWZ0bzloWkt0Wmx0czNERzNNMEFFWmlSTHpaN21Ma25yWDF2WmhSWGJBRGJCZ01oSGNPcU9sN1E1bHpUaDh0QjhnQU5xZk5MTyUyQkUzRWJXYWd4aW1aWkJPJTJGNmsxNjRVRmppQU9EZ0UxUzZDYVBvSG5zbjJtTUZkc1hvYUhmbk14Qjk3ckozcEJTUFp2bFBGV2JZd0l2ZENzaElIdGZTOFZSTVV0akg3VTVTTDV4aFo2R09mS0RSSXo0WEt6UUF2cXRwMFBRJTNEJTNE",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
            }

            x = requests.get(merhaba, data=data, headers=headers)
            y = BeautifulSoup(x.text, "html.parser")

            sanersearchResultsRowClass = y.find_all(class_="searchResultsRowClass")

            sanersayac = 0
            data_list = []

            for tr in sanersearchResultsRowClass:
                sanertr = tr.find_all("tr")
                for tr in sanertr:
                    sanersayac = sanersayac + 1
                    sanersearchResultsLargeThumbnail = sanertr[sanersayac-1]
                        
                    title_element = sanertr[sanersayac-1].find(class_="classifiedTitle")
                    title = title_element.text.strip() if title_element else "Başlık Bulunamadı"

                    image_element = sanertr[sanersayac-1].find("img")
                    image_src = image_element["src"] if image_element else "Görsel Bulunamadı"

                    store_element = sanertr[sanersayac-1].find(class_="titleIcon")
                    store = store_element["title"] if store_element else "Mağaza Bulunamadı"

                    price_element = sanertr[sanersayac-1].find(class_="classified-price-container")
                    price = price_element.text.strip() if price_element else "Fiyat Bilgisi Bulunamadı"

                    date_element = sanertr[sanersayac-1].find(class_="searchResultsDateValue")
                    date = date_element.text.strip() if date_element else "Tarih Bilgisi Bulunamadı"

                    location_element = sanertr[sanersayac-1].find(class_="searchResultsLocationValue")
                    location = location_element.text.strip() if location_element else "Konum Bilgisi Bulunamadı"
                    data_list.append({
                        "title": title,
                        "image_src": image_src,
                        "store": store,
                        "price": price,
                        "date": date,
                        "location": location
                    })

with open("ilanlar.json", "w", encoding="utf-8") as file:
    json.dump(data_list, file, ensure_ascii=False, indent=4)
