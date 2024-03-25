class animal:
    limbs=4
    eyes=2
    def __init__(self,limbs,eyes):
        self.limbs=limbs
        self.eyes=eyes

    def printProperties(self):
         print("The properties are limbs: ",self.limbs,"and eyes: ",self.eyes)

    def speak(self):
       pass


class Dog(animal):
    toes="claws"
    def __init__(self,limbs,eyes,mytoes):
        super().__init__(limbs,eyes)
        self.toes="mytoes"
    def speak(self):
        print("I am a dog and i bark")


class Cat(animal):
    def __init__(self,limbs,eyes):
        super().__init__(limbs,eyes)
    def speak(self):
        print("I am a cat and i meow")

dog1=Dog(2,2,10)
dog1.printProperties()
dog1.speak()

cat1=Cat(3,"cat")
cat1.speak()
