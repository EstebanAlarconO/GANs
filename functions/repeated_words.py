
PATH = 'save/20230218/covid_tweets/cot_vanilla_dt-Ra_lt-rsgan_mt-ra_et-Ra_sl66_temp1_lfd0.0_T0218_0949_57/samples/'
file = open(PATH+'samples_ADV_01999.txt', 'r')
lines = []
for line in file:
    lines.append(line.split())

count = 0
repeated_lines= []
for line in lines:
    for i in range(len(line)):
        if i == (len(line)-1):
            continue
        else:
            if line[i] == line[i+1]:
                repeated_lines.append(lines.index(line)+1)
                count+= 1
                break
print(count, repeated_lines)