from IPython.display import clear_output
import random
import numpy as np

class Hangman():

    hangman_menu = Menu('Welcome to Hangman!', ['Start Playing', 'Edit Word Library', 'Exit'])

    @classmethod
    def main(cls):

        exit = False
        while True:
            cls.hangman_menu.show_menu()
            print('Enter your option.')
            option = UserInput.int_input(0, cls.hangman_menu.menu_length() - 1)

            if option == 0:
                clear_output()
                my_guess = Guess()
                my_guess.guess_main()
            elif option == 1:
                clear_output()
                WordLib.wordlib_main()
            elif option == 2:
                print('Exiting game...')
                print('Bye!')
                break
