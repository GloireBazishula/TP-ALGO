
class Fraction:
    def __init__(self, _num, _den):
        assert isinstance(_num, int) and isinstance(_den, int) and _den > 0, "le dénominateur être un entier strictement positif"
        self._num = _num
        self._den = _den
        
    def __str__(self):
        if self._den == 1:
            return str(self._num)
        else:
            return f"{self._num}/{self._den}"
    
    def eq(self, other):
        return self._num*other._den == other._num*self._den

#test
if __name__ == '__main__':
    
    
    F1 = Fraction(3, 4)
    F2 = Fraction(-8, 1)
    F3 = Fraction(2, 3)
    F4 = Fraction(21, 28)
    
    
    print(F1)
    print(F2)
    print(F3)
    print(F4)
    
    
    print(F1.eq(F3)) # Doit afficher False
    print(F2.eq(F4)) # Doit afficher False
    print(F1.eq(F1)) # Doit afficher True
    