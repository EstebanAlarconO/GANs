keywords_hashtags= { '#corona': 0,
                     '#coronavirus': 0,
                     '#covid': 0,
                     '#covid19': 0,
                     '#covid-19': 0,
                     '#sarscov2': 0,
                     '#covid_19': 0,
                     '#ncov': 0,
                     '#ncov2019': 0,
                     '#2019-ncov': 0,
                     '#pandemic': 0,
                     '#2019ncov': 0,
                     '#quarantine': 0,
                     '#flatteningthecurve': 0,
                     '#flattenthecurve': 0,
                     '#handsanitizer': 0,
                     '#lockdown': 0,
                     '#socialdistancing': 0,
                     '#workfromhome': 0,
                     '#workingfromhome': 0,
                     '#ppe': 0,
                     '#n95': 0,
                     '#covidiots': 0,
                     '#herdimmunity': 0,
                     '#pneumonia': 0,
                     '#chinesevirus': 0,
                     '#wuhanvirus': 0,
                     '#kungflu': 0,
                     '#wearamask': 0,
                     '#vaccine': 0,
                     '#vaccines': 0,
                     '#coronavaccine': 0,
                     '#coronavaccines': 0,
                     '#faceshield': 0,
                     '#faceshields': 0,
                     '#healthworker': 0,
                     '#healthworkers': 0,
                     '#stayhomestaysafe': 0,
                     '#coronaupdate': 0,
                     '#frontlineheroes': 0,
                     '#coronawarriors': 0,
                     '#homeschool': 0,
                     '#homeschooling': 0,
                     '#hometasking': 0,
                     '#masks4all': 0,
                     '#wfh': 0,
                     '#washurhands': 0,
                     '#washyourhands': 0,
                     '#stayathome': 0,
                     '#stayhome': 0,
                     '#selfisolating': 0}

import json
# Función que recibe como parámetro un archivo json de tipo {'llave' = num} entregar el mismo de forma ordenada
def sort_json(json):
    with open(json) as json_file:
        data = json.load(json_file)

    sortedDict = sorted(data.items(), key=lambda x: x[1], reverse=True)
    sort = {}
    for i in sortedDict:
        sort[i[0]] = i[1]

    with open("sort_json.json", "w") as outfile:
        json.dump(sort, outfile, indent=4)


'''
with open(json) as json_file:
    data = json.load(json_file)

sortedDict = sorted(data.items(), key=lambda x: x[1], reverse=True)
sort = {}
sort_keywords = {}
for i in sortedDict:
    sort[i[0]] = i[1]
    if i[0] in keywords_hashtags.keys():
        sort_keywords[i[0]] = i[1]
for key in keywords_hashtags.keys():
    if key not in sort_keywords.keys():
        sort_keywords[key] = 0

with open("sort_hashtags.json", "w") as outfile:
    json.dump(sort, outfile, indent=4)

with open("sort_keywords.json", "w") as outfile:
    json.dump(sort_keywords, outfile, indent=4)'''
