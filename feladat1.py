
#####################
# fuggvenyek        #
#####################

def beolvasas(filename):
  # Using readlines()
  file1 = open(filename, 'r')
  Lines = file1.readlines()
  file1.close()

  dictionary = {}

  count = 0
  # Strips the newline character
  for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
    line = line.rstrip() # remove newline characters
    line = line.strip() # remove leading and ending spaces
    line = line.replace(" ", "") # remove all ASCII spaces (U+0020)
    array = line.split(";")
    dictionary.setdefault(array[0], []).append(float(array[1]))
    dictionary.setdefault(array[0], []).append(float(array[2]))

  # dictionary.remove('key')
  # if 'value' in dictionary['key']
  # print(dictionary)

  return dictionary

def atdolgozas(adatok):

  Lista_honap = []
  Lista_literar = []

  for key, value in adatok.items():
    Lista_honap.append(key)
    Lista_literar.append(float(value[1]) / float(value[0])) # osszesen hany Eurot fizettunk, osztva a hany literrel -> 1 liter hany Euroba kerult

  return (Lista_honap, Lista_literar)

def iras(lista_honap, lista_literar, filename):
  f = open(filename, "w")

  fajlTartalom = ""

  # zip -> python3 feature, a rovidebb lista vegeteresekor megall
  for a, b in zip(lista_honap, lista_literar):
    fajlTartalom += (str(a) + ',' + str(b) + '\n')

  f.write(fajlTartalom)
  f.close()

########################
# fo resz              #
########################

dict = beolvasas("tanklista_2020.txt")
for key, value in dict.items():
  print('honap: ', key, ', benzinmennyiseg: ', value[0], ' (liter), benzinkoltseg: ', value[1], '(Euro)')

Lis_honap = []
Lis_literar = []
(Lis_honap, Lis_literar) = atdolgozas(dict)

iras(Lis_honap, Lis_literar, 'literar_2020.txt')
