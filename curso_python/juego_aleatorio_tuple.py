#piedra papel o tijera usando tuple
import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_win = 0
rounds = 1

while True:

  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)

  print('computer winner', computer_wins)
  print('User winner', user_win)

  user_option = input("Elije = piedra, papel o tijera ").lower()
  computer_option = random.choice(options)

  if not user_option in options:
    print('esa opcion no es valida')

  print('User option =>', user_option)
  print('Computer option =>', computer_option)

  if user_option == computer_option:
    print("empatados")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("piedra rompe tijera")
      print("usuario gano!")
      user_win += 1
    else:
      print("papel envuelve piedra")
      print("computer winner")
      computer_wins += 1
  elif user_option == "papel":
    if computer_option == "tijera":
      print("tijera corta papel")
      print("computadora gano!")
      computer_wins += 1
    else:
      print("papel envuelve a piedra")
      print("user winner")
      user_win += 1
  elif user_option == "tijera":
    if computer_option == "piedra":
      print("piedra gana a tijera")
      print("computadora gano!")
      computer_wins += 1
    else:
      print("tijera corta a papel")
      print("user winner")
      user_win += 1

  if computer_wins == 2:
    print('Computer es el rotundo ganador')
    break

  if user_win == 2:
    print('User es el rotundo ganador')
    break

  rounds += 1