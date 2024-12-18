import random

def number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Введите ваше предположение: "))
        attempts += 1
        if guess < number_to_guess:
            print("Загаданное число больше.")
        elif guess > number_to_guess:
            print("Загаданное число меньше.")
        else:
            print(f"Поздравляем! Вы угадали число за {attempts} попыток.")
            break

number()



def group(input_string):
    grouped_symbols = []
    for char in input_string:
        if not grouped_symbols or grouped_symbols[-1] != char:
            grouped_symbols.append(char)
        else:
            grouped_symbols.append(char)

    return grouped_symbols

input_string = "xcvibjndsfibivbsduvhsciyhcfirghtiyhibvuiuhijhtrc"
print(group(input_string))




import random

def play():
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)

    player = []
    computer = []

    def draw(hand):
        card = deck.pop()
        hand.append(card)
        return card

    def calculate(hand):
        score = 0
        aces = 0
        for card in hand:
            if card in ['J', 'Q', 'K']:
                score += 10
            elif card == 'A':
                aces += 1
                score += 11
            else:
                score += int(card)

        while score > 21 and aces:
            score -= 10
            aces -= 1

        return score

    def show(hand):
        return ', '.join(hand)

    for _ in range(2):
        draw(player)
        draw(computer)

    print(f"Ваша рука: {show(player)}")
    print(f"Рука компьютера: {computer[0]}, [скрыто]")

    while True:
        action = input("Хотите взять еще карту? (y/n): ").strip().lower()
        if action == 'y':
            draw(player)
            print(f"Ваша рука: {show(player)}")
            if calculate(player) > 21:
                print("Вы проиграли! Ваше количество очков больше 21.")
                return
        else:
            break
    while calculate(computer) < 17:
        draw(computer)

    print(f"Рука компьютера: {show(computer)}")

    player = calculate(player)
    computer = calculate(computer)

    print(f"Ваше количество очков: {player}")
    print(f"Количество очков компьютера: {computer}")

    if player > 21:
        print("Вы проиграли!")
    elif computer > 21:
        print("Вы выиграли!")
    elif player > computer:
        print("Вы выиграли!")
    elif computer > player:
        print("Вы проиграли!")
    else:
        print("Ничья!")

play()


