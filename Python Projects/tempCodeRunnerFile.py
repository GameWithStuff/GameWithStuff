class Animal:
    def __init__(this,species,name):
        this.name = name
        this.species = species
    def doTrick(this):
        print(f'{this.name} is going to speak')
        print(f'my name is {this.name} and i am a {this.species}')
class Cat(Animal):
        def __init__(this,name):
            this.name = name
            this.species = 'Cat'
        def Meow(this):
            for i in range(5):
                print('Meow!!!')
a = Animal('Pikachu','Weakling')
c = Cat('Meowth')
a.doTrick()
c.doTrick()
c.Meow()