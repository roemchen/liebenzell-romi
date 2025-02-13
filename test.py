class Person:
    def __init__(self, name, gewicht, jahr):
        self.name = name
        self.gewicht = gewicht
        self.jahr = jahr
    
    def grussen(self):
        return f"Hey, i´m {self.name}"
    


romi = Person("romi", 40, 2009)
print(romi.grussen())

vasco =  Person("vasco", 80, 1992)
print(vasco.name)
