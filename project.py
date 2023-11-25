import sys
import random
import cowsay

def main():
    score = 0
    chances = 3
    user = input("Provide username to continue! ")
    cowsay.cow(f" Hello {get_user(user)}, welcome to Guess the Capital, in this game you will be given the country and you will have to guess its capital.")
    started = start(score, chances)
    cowsay.cow(started)
    cont1 = continue_game(started)
    if cont1 == True:
        inter = intermediate_l(score, chances)
        cowsay.cow(inter)
    else:
        sys.exit("Thank you for playing the game.")
    cont2 = continue_game(inter)
    if cont2 == True:
        cowsay.cow(hard_l(score, chances))
    else:
        sys.exit("Thank you for playing the game.")

def get_user(s):
    while 2 >= len(s.strip()):
        s = input("Username should be more than 2 letters: ")
    while len(s.strip()) > 8:
        s = input("Username should be less than 8 characters: ")
    return s

def start(score, chances):
    easy = {
            "America": "washington d.c.",
            "Spain": "madrid",
            "Italy": "rome",
            "France": "paris",
            "Russia": "moscow",
            "Germany": "berlin",
            "Mexico": "mexico city",
            "United Kingdom": "london",
            "China": "beijing",
            "Japan": "tokyo",
        }

    print("There are 3 levels to complete. First, in easy one you have to guess 10 capitals, in intermediate and hard ones you have to guess only 5. Good Luck!!!")
    while score != 10:
        country, capital = random.choice(list(easy.items()))
        answer = input(f"What's the capital of {country}: ")
        if answer.lower() != capital:
            while True:
                if chances == 1:
                    sys.exit("Unfortunately you lost the game.")
                answer = input(f"Wrong, think harder, you got {chances - 1} chances left: ")
                chances = chances - 1
                if answer.lower() == capital:
                    score = score + 1
                    print(f"score: {score}")
                    easy.pop(country)
                    break
        else:
            easy.pop(country)
            score = score + 1
            print(f"score: {score}")
    return f"congratulations, you have completed the easy level."

def intermediate_l(score, chances):
    intermediate = {
            "Venezuela": "caracas",
            "Egypt": "cairo",
            "Austria": "vienna",
            "Thailand": "bangkok",
            "Belgium": "brussels",
            "Brazil": "brasilia",
            "Bulgaria": "sofia",
            "Armenia": "yerevan",
            "India": "new delhi",
            "Philippines": "manila"
        }
    while score != 5:
        country, capital = random.choice(list(intermediate.items()))
        answer = input(f"What's the capital of {country}: ")
        if answer.lower() != capital:
            while True:
                if chances == 1:
                    sys.exit("Unfortunately you lost the game.")
                answer = input(f"Wrong, think harder, you got {chances - 1} chances left: ")
                chances = chances - 1
                if answer.lower() == capital:
                    score = score + 1
                    print(f"score: {score}")
                    intermediate.pop(country)
                    break
        else:
            intermediate.pop(country)
            score = score + 1
            print(f"score: {score}")
    return f"congratulations, you have completed the intermediate level."

def hard_l(score, chances):
    hard = {
        "Afghanistan": "kabul",
        "Albania": "tirana",
        "Algeria": "algiers",
        "Andorra": "andorra la vella",
        "Sudan": "khartoum",
        "Georgia": "tbilisi",
        "Guinea": "conakry",
        "Ireland": "dublin",
        "Kenya": "nairobi",
        "Moldova": "chisinau"
    }
    while score != 5:
        country, capital = random.choice(list(hard.items()))
        answer = input(f"What's the capital of {country}: ")
        if answer.lower() != capital:
            while True:
                if chances == 1:
                    sys.exit("Unfortunately you lost the game.")
                answer = input(f"Wrong, think harder, you got {chances - 1} chances left: ")
                chances = chances - 1
                if answer.lower() == capital:
                    score = score + 1
                    print(f"score: {score}")
                    hard.pop(country)
                    break
        else:
            hard.pop(country)
            score = score + 1
            print(f"score: {score}")
    return f"congratulations, you have completed all of the levels."


def continue_game(an):
    if an == "congratulations, you have completed the easy level.":
        answ = input("Do you wish to continue to Intermediate level? y/n ").lower()
        while answ != 'y' and answ != 'n':
            answ = input("y/n ")
        if answ == 'n':
            return False
        else:
            return True
    elif an == "congratulations, you have completed the intermediate level.":
        answ = input("Do you wish to continue to hard level? y/n ").lower()
        while answ != 'y' and answ != 'n':
            answ = input("y/n ")
        if answ == 'n':
            return False
        else:
            return True



if __name__ == "__main__":
    main()