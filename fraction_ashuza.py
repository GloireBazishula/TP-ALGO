# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 10:36:58 2024

@author: bazish
"""

class Fraction:
    
    def __init__(self,_num, _den):
        self._num = _num
        
        if _den > 0:
            self._den = _den
        else:
            return "Denominateur doit etre > 0"
        
        

        