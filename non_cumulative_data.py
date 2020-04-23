import requests
import csv

url = "https://pomber.github.io/covid19/timeseries.json"
covid = requests.get(url).json()
exporter = csv.writer(open("Newcases_Data.csv","w"), lineterminator = '\n')
exporter.writerow(['Country','Date','Confirmed','Deaths','Recovered'])

for country in covid:
    previous_day_confirmed = 0
    previous_day_deaths = 0
    previous_day_recovered = 0
    for item in covid[country]:
        if country == "Taiwan*":
            country = "Taiwan"
        elif country == "US":
            country = "USA"
        confirmed_cases = item["confirmed"] - previous_day_confirmed
        previous_day_confirmed = item["confirmed"]
        death_cases = item["deaths"] - previous_day_deaths
        previous_day_deaths = item["deaths"]
        recovered_cases = item["recovered"] - previous_day_recovered
        previous_day_recovered = item["recovered"]
        exporter.writerow([
            country,
            item['date'],
            confirmed_cases,
            death_cases,
            recovered_cases
        ])
