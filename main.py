user_option = input("Elije = piedra, papel o tijera ").lower()
computer_option = "piedra"

if user_option == computer_option:
  print("empatados")
elif user_option == "piedra":
  if computer_option == "tijera":
    print("piedra rompe tijera")
    print("usuario gano!")
  else:
    print("papel envuelve piedra")
    print("computer winner")
elif user_option == "papel":
  if computer_option == "tijera":
    print("tijera corta papel")
    print("computadora gano!")
  else:
    print("papel envuelve a piedra")
    print("user winner")
elif user_option == "tijera":
  if computer_option == "piedra":
    print("piedra gana a tijera")
    print("computadora gano!")
  else:
    print("tijera corta a papel")
    print("user winner")