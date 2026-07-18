"""
Animal nomli abstract class yarating.
Unda: Sound() nomli abstract metod bo'lsin.
Bola classlar: Dog → Sound() → "Vov-vov!", Cat → Sound() → "Miyov!"
Obyektlar yaratib Sound() metodlarini chaqiring.
"""
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def Sound(self):
        pass

class Dog(Animal):
    def Sound(self):
        print("Vov-vov!")

class Cat(Animal):
    def Sound(self):
        print("Miyov!")

dog = Dog()
cat = Cat()

dog.Sound()
cat.Sound()