class Guess():

    def __init__(self):
        self.answer = WordLib.random_word()
        self.remaining = list(set(''.join(self.answer.split())))
        self.num_attempts = len(self.remaining) + 5
        self.num_hints = len(self.remaining) - 1
        self.curr_guess = self.init_guess()
        self.history = set()

    def init_guess(self):
        init_guess = ['_'] * len(self.answer)
        for i, letter in enumerate(self.answer):
            if letter == ' ':
                init_guess[i] = ' '
        curr_guess = init_guess
        return curr_guess

    def add_history(self, a_letter):
        self.history.add(a_letter)

    def print_history(self):
        print('History: '.format(list(self.history)))

    def get_guess(self):
        return UserInput.letter_input()

    def hide_answer(self):
        out = ''
        if self.answer is None:
            print('Initialize a answer first!')
            return
        for letter in self.answer:
            if letter.isalpha():
                out = out + '_ '
            elif letter == ' ':
                out = out + '  '
        print(out)

    def show_guess(self):
        #print('==========================================')
        out = ' '.join(self.curr_guess)
        print(' ')
        print(out)
        print('==========================================')

    def show_stats(self):
        print('==========================================')
        print('You have {} attempts left.'.format(self.num_attempts))
        print('You have {} hints left.'.format(self.num_hints))

    def update_guess(self, guess_letter):
        self.num_attempts -= 1
        if guess_letter.lower() not in self.answer.lower():
            return False
        else:
            for i in range(len(self.answer)):
                if self.curr_guess[i] == '_' and self.answer[i].lower() == guess_letter.lower():
                    self.curr_guess[i] = self.answer[i]
                elif self.answer[i].lower() == ' ':
                    self.curr_guess[i] = ' '
            return True

    def check_answer(self):
        print('==========================================')
        return ''.join(self.curr_guess) == self.answer

    def give_hint(self):
        return self.remaining[-self.num_hints]

    def guess_main(self):
        #self.hide_answer()
        exit = False
        is_in = None
        user_guess = None
        has_hint = None

        while self.num_attempts >= 0 and not exit:

            if self.num_attempts == 0:
                clear_output()
                WordLib.show_word_info(self.answer)
                self.show_guess()
                self.show_stats()
                print('Sorry, you have used all the attempts.')
                print('The answer is: {}'.format(self.answer))
                print('Good luck next time!')
                exit = True
                break

            clear_output()
            print('==========================================')
            print('Playing Hangman...')
            print('==========================================')

            # print a notice: '' is in the word or not
            if is_in == True:
                print('Good job! \'{}\' is in this word!'.format(user_guess))
            elif is_in == False:
                print('Try again! \'{}\' is not in this word!'.format(user_guess))
            is_in = None

            # print a notice: '' is in the word
            if has_hint == True:
                print('Hint: \'{}\' is in this word!'.format(user_hint))
            elif has_hint == False:
                print('Sorry, you have used all the hints.')

            WordLib.show_word_info(self.answer)
            self.show_guess()
            self.show_stats()
            play_options = Menu('Play Option', ['Try my luck', 'Give me a hint', 'Give up'])
            play_options.show_menu()
            print('Enter your option.')
            option = UserInput.int_input(0, play_options.menu_length() - 1)


            if option == 0:
                clear_output()
                WordLib.show_word_info(self.answer)
                self.show_guess()
                self.show_stats()
                user_guess = self.get_guess()
                is_in = self.update_guess(user_guess)
                #continue
                if self.check_answer():
                    clear_output()
                    print('==========================================')
                    self.show_guess()
                    print('Congratulations! You win!')
                    print('The answer is: {}'.format(self.answer))
                    print('Returning to main menu...')
                    exit = True
                    break

            elif option == 1:
                has_hint == None
                if self.num_hints > 0:
                    self.num_hints -= 1
                    self.show_guess()
                    self.show_stats()
                    user_hint = self.give_hint()
                    has_hint = self.update_guess(user_hint)
                    #has_hint = True
                    self.num_attempts += 1
                    #continue
                    if self.check_answer():
                        clear_output()
                        print('==========================================')
                        self.show_guess()
                        print('Congratulations! You win!')
                        print('The answer is: {}'.format(self.answer))
                        print('Returning to main menu...')
                        exit = True
                        break
                else:
                    self.num_hints = 0
                    #print('Sorry, you have used all the hints.')
                    has_hint = False


            elif option == 2:
                clear_output()
                print('==========================================')
                print('Playing Hangman...')
                print('==========================================')
                self.show_guess()
                print('You almost there!')
                print('The answer is: {}'.format(self.answer))
                print('Good luck next time!')
                print('Returning to main menu...')
                exit = True
                break
