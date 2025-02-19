#!/usr/bin/env python3

import pruebas

def test():
    """Unit test for do_helloworld function"""
    # run the function to test and recover its output
    check_output = pruebas.do_helloworld()
    # verify the output
    if check_output == "Hello World": 
        print("Test is OK")
    else: 
        print('"Test is not OK! expected a "Hello world"')
        print(f'.. but received {check_output}')

if __name__ == "__main__":
    test()

