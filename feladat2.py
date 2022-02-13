
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

########################
# fo resz              #
########################

VWGolf = Jarmu("VW Golf", 50, 6.3)
print(VWGolf.tankterfogat, VWGolf.fogyasztas)
print(VWGolf.get_fuellstand())

# ez volt a feladatban
VWGolf.utazas(100.0) # utazunk 100 km-t
print(VWGolf.get_fuellstand()) # 100 km-nyi utazas utan, ennyi benzinunk marad a tankban

# extra
VWGolf.utazas(100.0) # utazunk ujabb 100 km-t
print(VWGolf.get_fuellstand()) # ujabb 100 km-nyi utazas utan, ennyi benzinunk marad a tankban

# extra
VWGolf.utazas(100.0) # utazunk ismet ujabb 100 km-t
print(VWGolf.get_fuellstand()) # ismetelten ujabb 100 km-nyi utazas utan, ennyi benzinunk marad a tankban

print(VWGolf.__str__())
