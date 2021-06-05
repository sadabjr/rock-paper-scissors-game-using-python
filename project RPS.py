import random
print("Hay buddy welcom in this game !")
print('''
╭━━━╮╱╱╱╱╱╭╮╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━━━╮
┃╭━╮┃╱╱╱╱╱┃┃╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃
┃╰━╯┣━━┳━━┫┃╭╮╱┃╰━╯┣━━┳━━┳━━┳━╮╱┃╰━━┳━━┳┳━━┳━━┳━━┳━┳━━╮
┃╭╮╭┫╭╮┃╭━┫╰╋┻━┫╭━━┫╭╮┃╭╮┃┃━┫╭┻━╋━━╮┃╭━╋┫━━┫━━┫╭╮┃╭┫━━┫
┃┃┃╰┫╰╯┃╰━┫╭╋┳━┫┃╱╱┃╭╮┃╰╯┃┃━┫┣━━┫╰━╯┃╰━┫┣━━┣━━┃╰╯┃┃┣━━┃
╰╯╰━┻━━┻━━┻╯╰╯╱╰╯╱╱╰╯╰┫╭━┻━━┻╯╱╱╰━━━┻━━┻┻━━┻━━┻━━┻╯╰━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯''')
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images=[rock, paper, scissors]
#rock(0) win against scissors(2)
#scissors(2) win against paper(1)
#paper(1) win against rock(0)

user_choice = int( input( "What is your choice, Enter 0 for rock, 1 for paper and 2 for scissors: " ))
print(game_images[user_choice])

computer_choice = int(random.randint(0, 2))
print(f"computer choice {computer_choice}")
print(game_images[computer_choice])


if user_choice>=3 or user_choice<0:
  print("You have made wrong choice, you loose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You loose!")
elif user_choice == 0 and computer_choice == 1:
    print("You loose!")
elif computer_choice < user_choice:
    print("You loose!")
elif computer_choice == user_choice:
    print("its draw!")
