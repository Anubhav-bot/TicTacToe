import os

inp = input("CLI or GUI? \n").upper()

if inp == 'CLI' or inp == 'C':
  if os.name == 'posix':    
    _ = os.system('python3 CLI.py')
  else:
    _ = os.system('python CLI.py')
    
elif inp == 'GUI' or inp == 'G':
  try:
    import pygame
  except:
    _ = os.system('pip3 install pygame')
    
  if os.name == 'posix':
    _ = os.system('python3 GUI.py')
  else:
    _ = os.system('python GUI.py')
