import os
import BinaryTree as bt
import subprocess

try:
    while (True):
        checkerInput = input("Ingrese la cadena: ")
        if(checkerInput == ''):
            print('Invalid Output')
            continue
        checkerOutput = subprocess.Popen(["./checker"], stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                         shell=True, universal_newlines=True)
        checkerOutput.stdin.write(str(checkerInput))
        checkerOutput = checkerOutput.communicate()[0].strip()
        if(checkerOutput == 'Nothing'):
            print('Invalid Output')
        else:
            print(bt.createNode(checkerInput))
            print('Result: ' + checkerOutput.split(' ')[1])

except KeyboardInterrupt:
    pass
