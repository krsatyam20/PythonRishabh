#inheritance

'''  more than two class one has parent and second has child

child inherit property of parent
'''


class animal:
    def eat(sa):
        print("parent class")
    def drink(xy):
        print("Drink Water")

    
class human(animal):
    def song(ha):
        print("singing a song ")

class boy(human):
    def movie(m):
        print("Watching movie")
h=boy()
h.song()
h.eat()
h.drink()













