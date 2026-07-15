"""
Class5
Rectangle klassi tuzilsin. Unda A va B tomonlari bo'lsin. 
Area() metodi to'g'ri to'rtburchak yuzini hisoblasin. 
Berilgan tomonlar uchun Area() metodi qiymati chop qilinsin

"""
class Rectangle:
    
    def __init__(self, A, B):
        self.A = A
        self.B = B
        
    def Area(self):
        return self.A * self.B
    
shakl = Rectangle(10, 12) 

print(shakl.Area())   
        
        

