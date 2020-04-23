import requests
import csv
import schedule
import time
url = "https://pomber.github.io/covid19/timeseries.json"


def update():
    covid = requests.get(url).json()
    exporter = csv.writer(open("../COVID19Data.csv", "w"), lineterminator ="\n")
    exporter.writerow(["Country", "Date", "Confirmed", "Deaths", "Recovered"])
    for country in covid:
        print(country)
        for item in covid[country]:
            if country == "Taiwan*":
                country = "Taiwan"
            elif country == "US":
                country = "USA"
            exporter.writerow([
                country,
                item["date"],
                item["confirmed"],
                item["deaths"],
                item["recovered"]
            ])


schedule.every().day.at("14:31").do(update)
while True:
    schedule.run_pending()
    time.sleep(60)