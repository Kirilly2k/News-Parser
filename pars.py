from bs4 import BeautifulSoup
import requests
import csv
import os
csv_file = "news.csv"
if os.path.exists(csv_file):
    os.remove(csv_file)
count = 0
dict_topic = {"politics/":"Политика","economy/":"Экономика","world/":"Мир","society/":"Общество","incidents/":"Происшествия","defense_safety/":"Армия","science/":"Наука","culture/":"Культура","religion/":"Религия","tourism/":"Туризм"}
with open("news.csv","w",encoding="utf-8-sig") as file:
            file_writer = csv.writer(file, delimiter=",", lineterminator="\r")
            file_writer.writerow(["id","Категория","Название","Время публикации","Ссылка"])
for i in dict_topic.keys():
    with open("news.csv","a",encoding="utf-8-sig") as file:
            file_writer = csv.writer(file, delimiter=",", lineterminator="\r")
            file_writer.writerow([])
    url = "https://ria.ru/" + i
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
        }

    req = requests.get(url, headers=headers)
    src = req.text

    with open("page.html", "w", encoding="utf-8-sig") as file:
        file.write(src)
    soup = BeautifulSoup(src, "lxml")
    title = soup.find_all("a", class_="list-item__title")
    time = soup.find_all(class_="list-item__date")
    time_gen = (i.text for i in time)
    for d in title:
        count += 1
        link = d.get("href")
        c = d.text
        title = dict_topic[i]
        with open("news.csv","a",encoding="utf-8-sig") as file:
            file_writer = csv.writer(file, delimiter=",", lineterminator="\r")
            file_writer.writerow([count,title,c,next(time_gen),link])
        print(link)





