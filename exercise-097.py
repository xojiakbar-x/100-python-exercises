"""
Vehicle nomli ota class yarating.

Unda:
Move() metodi "Transport harakatlanmoqda." deb chiqarsin.

Bola classlar:
Car → "Mashina yurmoqda."
Plane → "Samolyot uchmoqda."
Boat → "Kema suzmoqda."

Barcha obyektlarni ro'yxatga joylab, Move() metodini chaqiring.
"""

class Vehicle:
    def Move(self):
        print("Transport harakatlanmoqda.")

class Car(Vehicle):
    def Move(self):
        print("Mashina yurmoqda.")
        
class Plane(Vehicle):
    def Move(self):
        print("Samolyot uchmoqda.")
        
class Boat(Vehicle):
    def Move(self):
        print("Kema suzmoqda.")
        
car = Car()
plane = Plane()
boat = Boat()

transports = [car, plane, boat]

for transport in transports:
    transport.Move()