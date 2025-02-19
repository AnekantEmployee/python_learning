from typing import List, Tuple, Dict, Union

# do not enforce types at runtime

n:int = 5
print(n.real)

name:str = "AJ"
print(name.format())

def sum(a: int, b: int) -> int:
    return a + b;
print(sum(1,2))

numbers: List[int] = [1,2,3,4]

person: Tuple[int, int, int] = ("AJ", 25, 1.5)
print(person) 

n = "String"
print(n)