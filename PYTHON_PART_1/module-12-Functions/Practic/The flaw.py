'Task 5. Imperfection'

# You came to work for a game development company, the target audience is children and their parents. The previous programmer had a task to make two games in one application so that the user could choose one of them. However, the programmer you took over didn't have time to complete this task before you were fired and left only a small project template.

# The rules of the game "Rock, paper, scissors": the program asks the user for a string and outputs whether he won or lost. Stone beats scissors, scissors cut paper, paper covers stone.

# The rules of the game "Guess the number": the program asks the user for a number until he guesses the riddle.
# What needs to be done

# Using this project template, implement the games "Rock, Paper, Scissors" and "Guess the Number".

# def rock_paper_scissors():
# # There will be a Rock, Paper, Scissors game here

# def guess_the_number():
# # There will be a "Guess the number" game here

# def main_menu():
# # Here is the main menu of the game

# main_menu()

# -----------------------------------------------

'Задача 5. Недоделка'

# Вы пришли на работу в компанию по разработке игр, целевая аудитория — дети и их родители. У предыдущего программиста было задание сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них. Однако программист, на место которого вы пришли, перед увольнением не успел выполнить эту задачу и оставил только небольшой шаблон проекта.

# Правила игры «Камень, ножницы, бумага»: программа запрашивает у пользователя строку и выводит, победил он или проиграл. Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.

# Правила игры «Угадай число»: программа запрашивает у пользователя число до тех пор, пока он не угадает загаданное.
# Что нужно сделать

# Используя этот шаблон проекта, реализуйте игры «Камень, ножницы, бумага» и «Угадай число».

# def rock_paper_scissors():
#   # Здесь будет игра «Камень, ножницы, бумага»

# def guess_the_number():
#   # Здесь будет игра «Угадай число»

# def main_menu():
#   # Здесь главное меню игры

# main_menu()

# ----------------------------------------------

def rock_paper_scissors(choice_gamer):
    choice_opponent = "ножницы"
    if choice_gamer == choice_opponent:
        print("Ничья!")
    elif choice_gamer == "камень":
        print("Вы выиграли!")
    else:
        print("Вы проиграли!")

def guess_the_number(user_number, secret_number):
    if user_number == secret_number:
        print("Вы угадали число! Поздравляем!")
        return True
    else:
        print("Не угадали. Попробуйте ещё раз")
        return False

def main_menu(choice_user):
    if choice_user == 1:
        print("КАМЕНЬ, НОЖНИЦЫ, БУМАГА")
        choosing_weapon = input("Выберите камень, ножницы или бумага: ") 
        rock_paper_scissors(choosing_weapon)
    elif choice_user == 2:
        print("УГАДАЙ ЧИСЛО")
        secret_number = 7
        guessed_correctly = False
        while not guessed_correctly:
            guessed_number = int(input("Угадайте число от 1 до 10: "))
            guessed_correctly = guess_the_number(guessed_number, secret_number)

print("МЕНЮ ИГР")
game_selection = int(input("1 - Камень, ножницы, бумага\n"
                         "2 - Угадай число\n"
                         "Выберите игру: "))

main_menu(game_selection)










  

