import os
import BinaryTree as bt
import subprocess

try:
    checkerInput = input("Ingrese la cadena: ")
    checkerOutput = subprocess.Popen(["./checker"], stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                     shell=True, universal_newlines=True)
    checkerOutput.stdin.write(str(checkerInput))
    checkerOutput = checkerOutput.communicate()[0].strip()
    print(bt.createNode(checkerInput))
    print(checkerOutput)
except KeyboardInterrupt:
    pass
