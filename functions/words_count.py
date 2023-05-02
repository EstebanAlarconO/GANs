import json 

def listaPalabrasDicFrec(listaPalabras):
    frecuenciaPalab = [listaPalabras.count(p) for p in listaPalabras]
    return dict(list(zip(listaPalabras,frecuenciaPalab)))

PATH = 'save/20230227/covid_tweets/maligan_vanilla_dt-Ra_lt-rsgan_mt-ra_et-Ra_sl66_temp1_lfd0.0_T0227_0157_09/samples/'
FILE = ['samples_ADV_00007', 'samples_ADV_00013', 'samples_ADV_00014']
extension = '.txt'

for i in FILE:
    archivo = open(PATH+i+extension, 'r')
    linea_palabras = ''
    contador = 0
    for linea in archivo:
        linea_palabras += linea
    lista_palabras = linea_palabras.split()

    with open("samples_json/words_count/20230227_MaliGAN_"+i+".json", "w") as outfile:
        json.dump(listaPalabrasDicFrec(lista_palabras), outfile, indent=4)

