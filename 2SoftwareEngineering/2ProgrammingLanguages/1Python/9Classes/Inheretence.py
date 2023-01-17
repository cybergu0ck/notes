
speak = "Bark" #global variable

class Animals:
    likes_food = "YES"  #local variable
    
    def __init__(self,name, is_pet):
        self.name = name
        self.is_pet = is_pet
    
class Dogs(Animals):                        # Animals is Super Class and Dogs is Sub Class
    def __init__(self, name, is_pet):
        Animals.__init__(self, name, is_pet)
       # speak = "Bark"

d1 = Dogs("Brownie", True)
print(d1.name + " likes to " + speak)

