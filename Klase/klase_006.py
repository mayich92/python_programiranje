
class TV:
    '''Definicija klase TV uređaja'''
    def __init__(self, dijagonala, proizvodac, model, soba, glasnoca=0, program=0, je_ukljucen=False):
        self.dijagonala = dijagonala
        self.proizvodac = proizvodac
        self.model = model
        self.soba = soba
        self.glasnoca = glasnoca
        self.program = program
        self.je_ukljucen = je_ukljucen
    
    def ukljuci(self):
        if not self.je_ukljucen:
            self.je_ukljucen = True
            # self.program = 1
            # self.glasnoca = 15
    
    def promijeni_program(self, prg):
        self.program = prg

    def podesi_glasnocu(self, smjer_promjene):
        if smjer_promjene == '+':
            self.glasnoca += 1
        elif smjer_promjene == '-':
            self.glasnoca -= 1
        elif smjer_promjene == '0':
            self.glasnoca = 0
    

tv1 = TV(45, 'Samsung', 'UE12312345', 'dnevni boravak', 10, 3, False)
print(tv1.je_ukljucen)
tv1.ukljuci()
print(tv1.je_ukljucen)

print(tv1.program)
tv1.promijeni_program(4)
print(tv1.program)

print(tv1.glasnoca)
tv1.podesi_glasnocu('+')
tv1.podesi_glasnocu('+')
tv1.podesi_glasnocu('+')
print(tv1.glasnoca)
tv1.podesi_glasnocu('0')
print(tv1.glasnoca)

print('-'*50)
tv2 = TV(55, 'Sony', 'KDASDUIZA17', 'spavaća soba')
print(tv2.glasnoca)