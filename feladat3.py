#####################
# osztalyok         #
#####################

class Jarmu:
  def __init__(self, elnevezes, tankterfogat, fogyasztas):
    self.elnevezes = elnevezes
    self.tankterfogat = tankterfogat # literben ertendo
    self.__fuellstand = tankterfogat # literben ertendo, privat (mert __ van elotte)
    self.fogyasztas = fogyasztas # "liter / 100km"-ben ertendo

  def __str__(self):
    return (self.elnevezes+ ': ' + str(self.fogyasztas) + ' litert fogyaszt 100km-en')

  # a fuellstand a jelenlegi rendelkezesre allo benzinmennyiseget jelenti
  def get_fuellstand(self):
    return self.__fuellstand

  def utazas(self, tavolsag):
    self.__fuellstand -= self.fogyasztas / 100.0 * tavolsag # a feladatban rossz volt a keplet, egyenlo helyett minuszegyenlo kell!!!

class Haszonjarmu(Jarmu):
  def __init__(self, elnevezes, tankterfogat, fogyasztas, terheles):
    super().__init__(elnevezes, tankterfogat, fogyasztas)
    self.terheles = terheles

  def __str__(self):
    return (self.elnevezes+ ' = fogyasztasa ' + str(self.fogyasztas) + ' Liter 100 kilometerenkent, ' + str(self.terheles) + ' kg a terheles')

  # A feladat szovegeben __it__ volt, de olyan nincs, gondolom itt __lt__ -re kell gondolni, mert olyan meg van.
  def __lt__(self, other):
    return self.terheles < other.terheles

  def __gt__(self, other):
    return self.terheles > other.terheles

  def __le__(self, other):
    return self.terheles <= other.terheles

  def __ge__(self, other):
    return self.terheles >= other.terheles

  def __eq__(self, other):
    return self.terheles == other.terheles

  def __ne__(self, other):
    return self.terheles != other.terheles

########################
# fo resz              #
########################

FordTransit = Haszonjarmu("Ford Transit", 72.0, 9.4, 800.0)

print(FordTransit)

MercedesSprinter = Haszonjarmu("Mercedes Sprinter", 100.0, 15.4, 1005.0)

print(MercedesSprinter > FordTransit) # ez itt True, mint a feladat szovegeben

print(MercedesSprinter > FordTransit) # ez is True, a feladat szovege hibasan False-t ir, a feladat szovege hibas/rossz
