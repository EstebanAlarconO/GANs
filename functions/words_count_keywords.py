import json

PATH = ''#'save/20230218/covid_tweets/cot_vanilla_dt-Ra_lt-rsgan_mt-ra_et-Ra_sl66_temp1_lfd0.0_T0218_0949_57/samples/'
FILE = ['covid_tweets_sample']#['samples_ADV_00500', 'samples_ADV_00600', 'samples_ADV_01999']
extension = '.txt'

for i in FILE:
    keywords = {'corona': 0,
            'coronavirus': 0,
            'covid': 0,
            'covid19': 0,
            'covid-19': 0,
            'sarscov2': 0,
            'sars cov2': 0,
            'sars cov 2': 0,
            'covid_19': 0,
            'ncov': 0,
            'ncov2019': 0,
            '2019-ncov': 0,
            'pandemic': 0,
            '2019ncov': 0,
            'quarantine': 0,
            'flatten the curve': 0,
            'flattening the curve': 0,
            'hand sanitizer': 0,
            'lockdown': 0,
            'social distancing': 0,
            'work from home': 0,
            'working from home': 0,
            'ppe': 0,
            'n95': 0,
            'covidiots': 0,
            'herd immunity': 0,
            'pneumonia': 0,
            'chinese virus': 0,
            'wuhan virus': 0,
            'kung flu': 0,
            'wearamask': 0,
            'wear a mask': 0,
            'vaccine': 0,
            'vaccines': 0,
            'corona vaccine': 0,
            'corona vaccines': 0,
            'face shield': 0,
            'face shields': 0,
            'health worker': 0,
            'health workers': 0,
            'wash ur hands': 0,
            'wash your hands': 0,
            'self isolating': 0}
    file = open(PATH+i+extension, 'r')
    lines = []
    for line in file:
        lines.append(line.split('\n')[0]+ ' ')
    for key, value in keywords.items():
        count=0
        for line in lines:
            count += line.count(key+ ' ')
            keywords[key] = value + count
                  
    with open("samples_json/words_count_keywords/"+i+".json", "w") as outfile:
        json.dump(keywords, outfile, indent=4)