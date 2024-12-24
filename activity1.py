class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def make_sound(self):
        print("Dog barks at strangers",)

class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def make_sound(self):
        print("Cat makes sound meow")

d1=dog("Greg",4)
c1=cat("Oreo",3)

for animal in (d1,c1):
    animal.make_sound()