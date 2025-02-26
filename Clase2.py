#forma 1 para definir atributos
class Mascota:
    nombre = ""
    especie = ""
    raza = ""
    edad = ""
    #forma 2 para definir atributos
    #Si no especifican el atributo se toman los que se especifican
    def __init__(self, nombre, especie="perro", raza="doberman", edad=10):
        """Constructor de la calse Mascota"""
        self.nombre= nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
    
    def habla(self):
        """Muestra mensaje de mascota"""
        print (f"soy '{self.nombre}' de la especie '{self.especie}' de raza '{self.raza}' y edad '{self.edad}' años")
        
        if self.especie.lower() == "perro":
            print(f"hago 'Guau!'")
        elif self.especie.lower() == "gato":
            print(f"hago 'Miau!'")
        else: 
            print(f"hago 'No se que soy :('")

m1 = Mascota("Firu")
m1.habla()
m2 = Mascota("Michi", "gato", "siames", 2)
m2.habla()
