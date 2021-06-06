import os

inp = input("CLI or GUI? \n").upper()

if inp == 'CLI' or inp == 'C':
  _ = os.system('python3 CLI.py')

elif inp == 'GUI' or inp == 'G':
  try:
    import pygame
  except:
    _ = os.system('pip3 install pygame')
  _ = os.system('python3 GUI.py')
