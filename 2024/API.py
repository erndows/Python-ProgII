import requests
import json

response = requests.get("https://restcountries.com/v3.1/all?fields=name,population,area,subregion,borders")
responseLV = requests.get("https://restcountries.com/v3.1/name/latvija")
print(response.status_code)
responseParsed=json.loads(response.text)
responseParsedLV=json.loads(responseLV.text)
allPopulation = 0
amount = 0
populationMax = -1
allArea = 0
subRegionLV =''
bordersLV = []
for country in responseParsed:
    print(country['name']['common'])
    amount += 1
    allPopulation += country['population']
    allArea += country['area']
    if populationMax < country['population']:
        populationMax = country['population']

for countryLV in responseParsedLV:
    subRegionLV = countryLV['subregion']
    bordersLV = countryLV['borders']

avgPop = allPopulation / amount


print(amount)
print(avgPop)
print(populationMax)
print(allArea)
print(subRegionLV)
print(bordersLV)