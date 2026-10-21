import json

class Tamagoshi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.alegria = 50
        self.vivente = True
        self.memoria = []

    def salvar_memoria(self, acao):

        self.memoria.append({
            "acao": acao
        })

        while len(self.memoria) > 3:
            self.memoria.pop(0)

        
        with open("memoria_tamagochi.json", "w") as f:
            json.dump(self.memoria, f, indent=4)

    def comer(self):
        if not self.vivente:
            print("seu bicho ta mortassooooooooo. lol.")
            return

        self.fome -= 10

        print(self.nome, "comeu")

        self.salvar_memoria("comeu")

    def resenhar(self):
        if not self.vivente:
            print("seu bicho ta mortassooooooooo. lol.")
            return

        self.alegria += 10

        print(self.nome, "resenhou")

        self.salvar_memoria("resenhou")

    def status(self):
        print("nome do seu pequeno animal:", self.nome)
        print("nível de alegria:", self.alegria)
        print("nível de fome:", self.fome)
        print("status de existência:", self.vivente)

    def possivel_morte(self):
        if self.fome >= 100 or self.alegria <= 0:
            self.vivente = False

    def salvar(self):
        emsumula = {
            "nome": self.nome,
            "fome": self.fome,
            "alegria": self.alegria,
            "vivente": self.vivente
        }

        with open("tamagoshi.json", "w") as f:
            json.dump(emsumula, f, indent=4)


















 

p = Tamagoshi("prikito")

p.resenhar() 
p.comer()
p.possivel_morte()
p.status()

p.salvar()

print("salvado loool")