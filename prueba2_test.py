#!/usr/bin/env python3

import prueba2

def test():
    """Unit test for do_helloworld function"""
    # run the function to test and recover its output
    check_output = prueba2.hello(f"{prueba2.nombre}")
    # verify the output
    if check_output == f"Hola Gabriel, ¿Cómo estas?": 
        print("Test is OK")
    else: 
        print(f'"Test is not OK! expected a "Hola Gabriel, ¿Cómo estas?"')
        print(f'.. but received {check_output}')

if __name__ == "__main__":
    test()