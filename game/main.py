import random

def choose_options():
  options = ("piedra", "papel", "tijera")
  user_option = input("Piedra, papel o tijera? => ")
  user_option = user_option.lower()
  
  if not user_option in options:
    print("Por qué elegirías esa idiotez?")
    return None, None
    #continue
  computer_option = random.choice(options)
  
  print("Elegiste => ", user_option)
  print("Martin Tetaz eligió => ", computer_option)
  return user_option, computer_option
  
def reglas(user_option, computer_option, user, martin_tetaz):
  if user_option == computer_option:
    print("Empate!")
  elif user_option == "piedra":
    if computer_option == "papel":
      print("Perdiste! :(")
      print("Papel le gana a piedra")
      martin_tetaz += 1
      print("Vos:", user)
      print("Martin Tetaz:", martin_tetaz)
    else:
      print("Ganaste! :)")
      print("Tijera le gana a papel")
      user += 1
      print("Vos:", user)
      print("Martin Tetaz:", martin_tetaz)
  elif user_option == "papel":
    if computer_option == "tijera":
      print("Perdiste! :(")
      print("Tijera le gana a papel")
      martin_tetaz += 1
      print("Vos:", user)
      print("Martin Tetaz:", martin_tetaz)
    else:
      print("Ganaste! :)")
      print("Papel le gana a piedra")
      user += 1
      print("Vos:", user)
      print("Martin Tetaz:", martin_tetaz)
  elif user_option == "tijera":
    if computer_option == "piedra":
      print("Perdiste! :(")
      print("Piedra le gana a tijera")
      martin_tetaz += 1
      print("Vos:", user)
      print("Martin Tetaz:", martin_tetaz)
    else:
      print("Ganaste! :)")
      print("Tijera le gana a papel")
      user += 1
      print("Vos:", user)
      print("Martin Tetaz:", martin_tetaz)
  return user, martin_tetaz

def run_game():
  user = 0
  martin_tetaz = 0
  rounds = 1
  while True:
    print("-" * 15)
    print("Round", rounds)
    print("-" * 15)
  
    print("Vos =>", user)
    print("Martin Tetaz =>", martin_tetaz)
    print("*" * 15)
    rounds += 1

    user_option, computer_option = choose_options()
    user, martin_tetaz = reglas(user_option, computer_option, user, martin_tetaz)
    
    if user == 2:
      print("Le ganaste al gran Martin Tetaz")
      break
    if martin_tetaz == 2:  
      print("El increible Martin Tetaz te rompio el orto")
      break

run_game()