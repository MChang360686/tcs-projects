import tkinter as tk
import math

def sum_ints(*nums: int) -> int:
    return sum(num for num in nums)
    
def sum_floats(*nums: float) -> float:
    return sum(num for num in nums)
    
def diff_ints(*nums: int) -> int:
    return sum(-num for num in nums)
    
def diff_floats(*nums: float) -> float:
    return sum(-n for num in nums)
    
def mult_ints(*nums: int) -> int:
    return math.prod(nums)
    
def mult_floats(*nums: float) -> float:
    return math.prod(nums)
    
def get_sqrt(num: int) -> int:
    return isqrt(num)
    
def get_sqrt_float(num: float) -> float:
    return sqrt(num)
    