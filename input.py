class Pessoa:
    def caracteristicas(self,nome,nascimento,peso):
        self.nome = nome
        self.nascimento = nascimento
        self.peso = peso 
    def askName():
        name  = input('Qual seu nome \n')
        return name
    def askBorn():
        born = input("Quando você nasceu?\n ")
        return born
    def askWeight():
        weight = input('Qual seu peso?\n')
        return weight    
    
pessoa2 = Pessoa()
pessoa2.caracteristicas(Pessoa.askName(),Pessoa.askBorn(),Pessoa.askWeight())
print('\nOlá {}!\nVocê nasceu em {} e tem {} Kg\n'.format(pessoa2.nome,pessoa2.nascimento,pessoa2.peso))
