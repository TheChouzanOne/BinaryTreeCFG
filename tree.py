import os
import BinaryTree as bt
import subprocess

try:
    system = input("Por favor indique su sistema operativo: [win|lin]: ")
    while(not (system == "win" or system == "lin")):
        system = input("Por favor indique su sistema operativo: [win|lin]: ")
    if(system == "lin"):
        checker = "./checker"
    elif(system == "win"):
        checker = "checker.exe"
    while (True):
        checkerInput = input("Ingrese la cadena: ")
        if(checkerInput == "quit"):
            break
        if(checkerInput == ''):
            print('Esa cadena no la reconoce nuestro lenguaje.')
            continue
        checkerOutput = subprocess.Popen([checker], stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                         shell=True, universal_newlines=True)
        checkerOutput.stdin.write(str(checkerInput))
        checkerOutput = checkerOutput.communicate()[0].strip()
        if(checkerOutput == 'Nothing'):
            print('Esa cadena no la reconoce nuestro lenguaje.')
        else:
            print(bt.createNode(checkerInput))
            print('Result: ' + checkerOutput.split(' ')[1])
except KeyboardInterrupt:
    print()
    pass
