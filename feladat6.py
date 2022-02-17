
#####################
# fuggvenyek        #
#####################

def olvasas(filename):
  # Using readlines()
  file1 = open(filename, 'r')
  Lines = file1.readlines()
  file1.close()

  dictionary = {}

  count = 0
  # Strips the newline character
  for line in Lines:

    # example line: "Antigua und Barbuda;St. John's,"

    count += 1
    print("Line{}: {}".format(count, line.strip()))
    line = line.rstrip() # remove newline characters
    line = line.strip() # remove leading and ending spaces
    line = line.replace(",", "") # remove all ',' characters
    
    # ASCII UTF-8 UTF-16 UTF-32 UNICODE
    
    line = line.replace('\r', "")
    line = line.replace('\n', "")

    array = line.split(";")
    dictionary.setdefault(array[0], []).append(array[1]) # key -> value, country -> capital

  # dictionary.remove('key')
  # if 'value' in dictionary['key']
  # print(dictionary)

  return dictionary

def mutasd_orszag(orszag, fovarosa): # itt nem biztos, hogy jól értettem a hibás fordítás alapján, hogy mit kér a feladat, nem biztos, hogy ezt :-)
  print(orszag + ' fővárosa ' + fovarosa)

def uj_orszag(szotar):
  
  print('Enter new country:')
  newCountry = input()

  for kulcs, ertek in szotar.items():
    if (kulcs == newCountry):
      print("mar felhasznalt orszag, nem modositjuk az adatszerkezetet")
      return szotar
  
  print('Enter new capital:')
  newCapital = input()

  for kulcs, ertek in szotar.items():
    if (ertek == newCapital):
      print("mar felhasznalt fovaros, nem modositjuk az adatszerkezetet")
      return szotar  
  
  szotar.setdefault(newCountry, []).append(newCapital)

  return szotar

def iras(szotar, filename):
  f = open(filename, "w")

  fajlTartalom = ""

  for key, value in szotar.items():
    fajlTartalom += (key + ";" + value[0] + "," + "\n") # nem írta a feladat, hogy nézzen ki a kimeneti fájl, de igazodok a bemeneti fájl szintaktikájához:    "Antigua und Barbuda;St. John's,"

  f.write(fajlTartalom)
  f.close()

########################
# fo resz              #
########################

dict = olvasas("HU_land_hauptstadt.txt")
for key, value in dict.items():
  print('orszag: ', key, ', fovarosa: ', value[0])

print("---")

for key, value in dict.items():
  mutasd_orszag(key, value[0])

dict = uj_orszag(dict)

print("---")

for key, value in dict.items():
  mutasd_orszag(key, value[0])

iras(dict, 'kimeneti_uj_fajl.txt')
