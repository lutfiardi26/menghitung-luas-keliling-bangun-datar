class Hero:
    def __init__(self,nama,darah,attackPower,armorNumber):
        self.nama = nama
        self.darah = darah
        self.attackPower = attackPower
        self.armorNumber = armorNumber
    
    def serang(self, Lawan):
        print(self.nama + ' menyerang ' + Lawan.nama)
        Lawan.diserang(self, self.attackPower)

    def diserang(self, Lawan, attackPower_Lawan):
        print(self.nama + ' diserang ' + Lawan.nama)
        attack_diterima = attackPower_Lawan/self.armorNumber
        print('serangan_terasa : ' + str(attack_diterima))
        self.darah -= attack_diterima
        print('darah' + self.nama + ' tersisa ' + str(self.darah))

Turtle = Hero('Turtle',100,12,4)
Lord = Hero('Lord',100,28,3)

Turtle.serang(Lord)
print('\n')
Lord.serang(Turtle)
print('\n')
Lord.serang(Turtle)
print('\n')
Lord.serang(Turtle)
print('\n')
Lord.serang(Turtle)
print('\n')
Lord.serang(Turtle)
print('\n')
