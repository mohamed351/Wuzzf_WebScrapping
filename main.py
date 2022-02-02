import bs4
import requests
import csv

job_list = []
tech_name = input("please Enter the Technology : ")
x = 0
while True:
    result = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q={tech_name}&start={x}")
    print("==================================")
    testing = bs4.BeautifulSoup(result.content, "lxml")
    content_div = testing.find_all("div", {"class": "css-1gatmva"})
    print(f"{len(content_div)} - >{x}")
    if len(content_div) == 0:
        break
    for item in content_div:
        job_list.append({"title": item.findNext("a", {"class": "css-o171kl"}).text,
                         "companyName": item.findNext("a", {"class": "css-17s97q8"}).text,
                         "location": item.findNext("span", {"class": "css-5wys0k"}).text,
                         "type": item.findNext("span", {"class": "eoyjyou0"}).text})
    x += 1

with open('testing.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["title", "companyName", "location", "type"])
    for item in job_list:
        writer.writerow([item.get("title"), item.get("companyName"), item.get("location"), item.get("type")])
