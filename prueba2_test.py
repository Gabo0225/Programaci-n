#!/usr/bin/env python3

import prueba2

def test():
    """Unit test for hello function"""
    # run the function to test and recover its output
    check_output = prueba2.hello(f"{prueba2.nombre}")
    # verify the output
    if check_output == prueba2.hello(f"Hola {prueba2.nombre}, ¿Cómo estas?"): 
        print("Test is OK")
    else: 
        print(f'"Test is not OK! expected a "Hola {prueba2.nombre}, ¿Cómo estas?"')
        print(f'.. but received {check_output}')

if __name__ == "__main__":
    test()