# Parent class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Child classes (inherits from Dog class)
class BullDog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

class AmericanBullDog(BullDog):
    def speak(self, sound):     # rewrite func
        return "{} don't wanna say anything".format(self.name)
    country = 'America'


# Child classes inherit attributes and behaviors from the parent class
jim = BullDog('Jim', 12)
print(jim.description())
print(jim.speak('Bye'))

# Child classes have specific attributes and behaviors
print(jim.run('slowly'))

print('-----')

# Double inherit
andy = AmericanBullDog('Andy', 7)
print(andy.country)
print(andy.speak("I'm hungrey"))   # test the rewrite function
