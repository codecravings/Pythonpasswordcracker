import random
import pyautogui


character_list=list("0123456789abcdefghijklmnopqrstuvwxyz")

password=pyautogui.password('Enter Password')

guess_password='  '

while (guess_password!=password):
    guess_password=random.choices(character_list,k=len(password))

    print(">>>>>"+str(guess_password)+"<<<<<")

    if (guess_password==list(password)):
        print("Your password us:"+"".join(guess_password))
        break
