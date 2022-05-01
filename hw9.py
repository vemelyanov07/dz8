import math

class treygol:
    a = int(input("Введите сторону a: "))
    b = int(input("Введите сторону b: "))
    c = int(input("Введите сторону c: "))
    p = (a+b+c)/2
    s = (c*c-b*b)**0.5
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))**0.5
    print(s)
    
    def storona(self):
        print(f"Треугольник построен: {self.s}")
        
    @property
    def storona1(self):
        print(f"Длина стороны а = {self.a}")
    
s = treygol()
s.storona()
a = treygol()
a.storona1


import json

def hw(homework: str):
    with open(f"{homework}.json", "r") as file:
        a = file.read()
        a = json.loads(a)
    return a

Class = type("Class", (), hw("homework"))

Num = Class()
print(f"{Num.firstName} {Num.lastName} {Num.hobbies}")