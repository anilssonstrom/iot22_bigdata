import json


class Cat:
    def __init__(self, age=0, name=None, sound="Meow", jumpiness=10, lives=7):
        self.lives = lives
        self.jumpiness = jumpiness
        self.sound = sound
        self.name = name
        self.age = age


luna = Cat(age=3, name='Luna', sound="Squeek", jumpiness=7, lives=5)
apollo = Cat(age=3, name='Apollo', sound="MEOOOOW", jumpiness=14, lives=7)

# Problem: Detta fungerar inte!
json.dumps(luna)
