import os
try:
  import pygame
except:
  _ = os.system('pip3 install pygame')

inp = input("CLI or GUI? \n").upper()

if inp == 'CLI' or inp == 'C':
  _ = os.system('python3 CLI.py')

elif inp == 'GUI' or inp == 'G':
  _ = os.system('python3 GUI.py')
