import random
from replit import clear
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):

  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "Ode preko. Svi gubite.😤"


  if user_score == computer_score:
    return "Izjednačeno!🙃"
  elif computer_score == 0:
    return "Gubite, protivnik ima Crnog Jacka!😱"
  elif user_score == 0:
    return "Pobjeda sa Crnim Jackom!😎"
  elif user_score > 21:
    return "Otišli ste preko 21, gubite.😭"
  elif computer_score > 21:
    return "Protivnik je otišao preko 21! Vi dobijate!😁"
  elif user_score > computer_score:
    return "Pobjedili ste!😃"
  else:
    return "Izgubili ste.😤"

def play_game():

  print(logo)

  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Vaše karte: {user_cards}, trenutni bodovi: {user_score}")
    print(f"   Protivnikova prva karta: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Utipkajte 'k' za izvlačenje karte ili 'n' za dalje: ")
      if user_should_deal == "k":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Vaše ukupne karte: {user_cards}, završni bodovi: {user_score}")
  print(f"   Protivnikove ukupne karte: {computer_cards}, završni bodovi: {computer_score}")
  print(compare(user_score, computer_score))

while input("Želite li zaigrati Crnog Jacka? Type 'd' or 'n': ") == "d":
  clear()
  play_game()
