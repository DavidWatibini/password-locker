#!/usr/bin/env python3.6
from user import User
import getpass
import random
import string

def create_account(account_name,username,password,confirm_password):

    """
    function to create a new account
    """

    new_user = User(account_name,username,password,confirm_password)

    return new_user

def save_details(user):

    """
    function to save save_details
    """
    user.save_detail()

def display_all_details():

    """
    function used to return all saved save_details
    """
    return User.display_all_details()

def check_existing_user(username):

    """
    a function that is used to check and return all exissting accounts
    """

    return User.user_exist(username)

def find_user(username):

    """
    the function is used check details from the saved save_details
    """

    return User.find_by_username(username)

def generatePassword(num):
   genpas = ''

   for n in range(num):
       x = random.randint(0,94)
       genpas += string.printable[x]

   return genpas

# def gen_word(min, max):
#     vowels = list('aeiou')
# 	word = ''
# 	syllables = min + int(random.random() * (max - min))
# 	for i in range(0, syllables):
# 		word += gen_syllable()
#
# 	return word.capitalize()
def main():
    print('{:_^5}'.format('RE-INVENT THE WAY YOU SAVE YOUR PASSWORDS WITH OUR PASSWORD LOCKER APP'))


    print('\n')

    print('{:_^20}'.format('login'))

    print('\n')

    print("please idetify yourself using your locker username")

    user_name = input().upper()

    print(f"Hello {user_name}, welcome to your password manager, how can we help you today")

    print('\n')

    while True:

        list =('''
        1-register a new account
        2-display accounts
        3-find accounts
        4-exit the locker\n''')
        print(list)



        short_code = input().lower()

        if short_code == '1':

            print(f"{user_name} please fill in the following")

            print("-"*10)

            print ("account name")
            account_name = input()

            print("username")
            username = input()

            print('\n')

            print("Do you want a randomly generated password?")


            print("yes", "no")
            ans = input().lower()

            if ans == 'yes':

                genpas = print(generatePassword(10))

                save_details(create_account(account_name,username,password,confirm_password))

                print ('\n')

                print(f"{user_name} {account_name} account of {username} created and password saved")

                print ('\n')


            elif ans == 'no':
                password = getpass.getpass('password:')
                print("*********")

                confirm_password = getpass.getpass('confirm password:')
                print("*********")

                save_details(create_account(account_name,username,password,confirm_password))

                print ('\n')

                print(f"{user_name} {account_name} account of {username} created and password saved")

                print ('\n')

                print(f"{user_name} what else do you want to do?")

        elif short_code =='2':


            if display_all_details():

                print(f"{user_name} here is a list of all your accounts")

                print('\n')

                for user in display_all_details():

                    print(f"{user.account_name} {user.username}......{user.password}")

                    print('\n')

            else:

                print('\n')

                print(f" {user_name} You dont seem to have any contacts saved yet")

                print('\n')

        elif short_code == '3':

            print(f"{user_name} Enter a username you want to search for")

            search_username = input()


            if check_existing_user(search_username):

                search_username = find_user(search_username)

                print(f"{search_username.account_name} {search_username.username}")

                print('-' * 20)

                print(f"password.......{search_username.password}")
            else:
                print(f"{user_name} That account does not exist")

        elif short_code == "4":

            print("Bye .......")

            break

        else:
            print("I really didn't get that. Please use the correct code")











if __name__ == '__main__':

    main()
