#####################
# osztalyok         #
#####################

class Vektor:
  def __init__(self, Lista):
    self.Lista = Lista
    self.__Dim = len(Lista) # dimenzió, privát

  def __add__(self, other):
    # adding two objects
    # a feladat szerint feltetelezhetjuk, hogy a ket vektor azonos dimenzioju

    # zip -> python3 feature, a rovidebb lista vegeteresekor megall
    uj_lista = []
    for a, b in zip(self.Lista, other.Lista):
      uj_lista.append(a + b)
    uj_vektor = Vektor(uj_lista)
    return uj_vektor

  def norm(self):
    euklidesziNorma = 0
    for x in self.Lista:
      euklidesziNorma += (x * x)
    return euklidesziNorma

########################
# fo resz              #
########################

v = Vektor([1, 2]) + Vektor([3, 4])
print(v.Lista)
