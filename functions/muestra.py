from random import randint

def muestra(data_file, total_data, total_muestra):
    total_samples = 0
    sample = []
    for i in range(0, total_data):
        number = randint(1, total_data)
        if number in sample:
            continue
        elif total_samples < total_muestra:
            sample.append(number)
            total_samples += 1
    sample.sort()

    PATH = 'dataset/'
    file = open(PATH+data_file, 'r')
    lines = []
    count = 0
    number_line = 1
    for line in file:
        if count < total_muestra:
            if sample[count] == number_line:
                lines.append(line)
                count += 1
        else:
            break
        number_line += 1 

    with open('sample_'+data_file, 'w') as f:
        for line in lines:
            f.write(line)

def create_data_test(data_file):
    PATH = 'dataset/'
    with open(PATH+data_file, 'r') as f:
        lines = f.readlines()

    # obtener la cantidad total de líneas del archivo original
    total_lines = len(lines)

    # calcular la cantidad de líneas para el 80% y 20%
    eighty_percent = []
    twenty_percent = []
    count = 0
    for i in range(total_lines):
        if count == 4:
            count = 0
            twenty_percent.append(lines[i])
        else:
            count += 1
            eighty_percent.append(lines[i])
    with open(PATH+'covid_tweets_3k.txt', 'w') as f1, open(PATH+'covid_tweets_3k_test.txt', 'w') as f2:
        f1.writelines(eighty_percent)
        f2.writelines(twenty_percent)

#muestra('covid_tweets_200k.txt', 160000, 3750)
create_data_test('sample_covid_tweets_200k.txt')