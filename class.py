lass Magicien:
  def __init__(self):
    self.point_vie = 100
    self.point_magie = 50
    self.point_deffence = 30
    self.point_attaque = 15

  def boire_potion(self):
    self.point_vie += 10 

  def boire_potion_magique(self):
    self.point_magie += 10

  def proteger(self):
    self.point_deffence -= 30

  def attaque(self,autre_magicien):
    self.point_attaque -=15
    autre_magicien.point_vie -= 10
    print("je n'ai plus  " + str(autre_magicien.point_vie)+ " point vie! ")

   

    if autre_magicien.point_vie > 0:
      print("je suis toujour en vie")

    else:
      print("j'ai perdu")



harry = Magicien()
jeason = Magicien()        

jeason.attaque(harry)

