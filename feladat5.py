
#####################
# osztalyok         #
#####################

# a feladat szovege a hibas forditas miatt nem volt egyertelmu, hogy a Vektor osztalyt oroklessel kell felhasznalni, vagy copy&paste-tel beepiteni a kodba, ugyhogy az utobbit csinaltam

class Ero:
  def __init__(self, Lista, m_tomeg, a_gyorsulas):
    self.Lista = Lista
    self.__Dim = len(Lista) # dimenzió, privát
    self.m_tomeg = m_tomeg
    self.a_gyorsulas = a_gyorsulas
    self.f_erovektor = m_tomeg * a_gyorsulas

  def __str__(self):
    return ('dimenzió: ' + str(self.__Dim) + ', tomeg: ' + str(self.m_tomeg) + ', gyorsulas: ' + str(self.a_gyorsulas) + ', f erovektor: ' + str(self.f_erovektor) + '\n')

  def __add__(self, other):
    # adding two objects
    # a feladat szerint feltetelezhetjuk, hogy a ket vektor azonos dimenzioju

    # zip -> python3 feature, a rovidebb lista vegeteresekor megall
    uj_lista = []
    for a, b in zip(self.Lista, other.Lista):
      uj_lista.append(a + b)
    uj_ero = Ero(uj_lista, self.m_tomeg + other.m_tomeg, self.a_gyorsulas + other.a_gyorsulas) # nem vagyok benne biztos, hogy a gyorsulasokat is ossze kell adni
    return uj_ero

  def norm(self):
    euklidesziNorma = 0
    for x in self.Lista:
      euklidesziNorma += (x * x)
    return euklidesziNorma

########################
# fo resz              #
########################

ero_1 = Ero([1, 2, 3], 100, 20)
ero_2 = Ero([4, 5, 6], 500, 3)
print(ero_1.__str__())
print(ero_2.__str__())

ero_3 = ero_1 + ero_2
print(ero_3.__str__())

norma = ero_3.norm()
print('norma: ' + str(norma))
