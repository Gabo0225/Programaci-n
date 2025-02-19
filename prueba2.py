

def hello(nombre):
    #saludar a alguien
    nombre = input ("¿Quien eres?¿Cómo te llamas?: ")
    output = f"Hola {nombre}, ¿Cómo estas?" 
    return output


def run():
    
    print (hello("nombre"))
if __name__ == "__main__":
    run()