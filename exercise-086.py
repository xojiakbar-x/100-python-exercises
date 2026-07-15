"""
Class6
Circle klassi tuzilsin. Unda R radius maydoni bo'lsin. 
Length() metodi aylana uzunligini hisoblasin. 
(Pi=3.14). Berilgan radius uchun aylana uzunligi chop qilinsin.
"""
class Circle:
    
    def __init__(self, R):
        self.R = R
        
    def Length(self):
        return 2*3.14*self.R
        
shakl = Circle(2)

print(shakl.Length())