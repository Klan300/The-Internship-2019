from random import randint
from time import time


def counting_score(time_first, number_guest, num_word):
    """
    count by time that player think and number of player guess
    if player think to long or guess but not the score will drop

    """
    raw_score = num_word * 30
    time_after = time()
    all_time = int(time_after - time_first)
    score = raw_score - (all_time * 2) - (number_guest * 3)
    if score <= 5:
        return 5
    else:
        return score


def count_word(word):
    """
    count the number of alphabet in word
    """
    count = 0
    for i in word:
        if i == '-' or i == ' ':
            pass
        else:
            count += 1
    return count

def check_int(ask):
    """
    check int input and ask again when input is not int but will  return if it was integer
    """
    while True:
        try:
            num = int(input(ask))
            return num
        except ValueError:
            print('input is not integer')
            print()


def openfile(text):
    """
    read file and return list of text file
    """
    file = open(text).read().splitlines()
    words = []
    for word in file:
        w = word.split('#')
        w.append(w[0])
        words.append(w)
    return words


def rand_word(words):
    """
    random word from list
    """
    num = randint(0, len(words) - 1)
    return words[num]


def choose_catagory():
    """
    choose catagory
    """
    choose = check_int('Choose catagory: ')
    while True:
        if choose == 1:
            text = 'Animal.txt'
            return text
        elif choose == 2:
            text = 'food.txt'
            return text
        else:
            choose = int(input('Choose catagory: '))


def create_question(word):
    """
    print question
    """
    for i in range(len(word[0])):
        if word[0][i] == '-':
            print('-', end='')
        elif word[0][i] == ' ':
            print(' ', end='')
        elif word[0][i] == '_':
            print(word[2][i], end='')
        elif word[0][i].isnumeric():
            print(word[0][i], end='')
        else:
            print('_', end='')


def console(word):
    """
    control one game and count the score
    """
    wrong_guess = []
    count_guess = 0
    score = 0
    num = count_word(word[0])
    vocab = word[0]
    attempt = 10
    time_start_guess = time()
    while True:
        if attempt >= 0:
            if word[0].count('_') < num:
                guess = ' '.join(wrong_guess)
                create_question(word)
                print(f'     score {score}, remaining wrong guess {attempt}, wrong guessed: {guess}')
                alphabet = input('>>> ')
                if not alphabet.isnumeric():
                    if len(alphabet) == 1:
                        if alphabet in vocab or alphabet in vocab.upper():
                            num_word = word[0].count(alphabet.lower())
                            word[0] = word[0].replace(alphabet.lower(), '_')
                            score += counting_score(time_start_guess, count_guess, num_word)
                            time_start_guess = time()
                            count_guess = 0
                            print('correct')
                        else:
                            count_guess += 1
                            try:
                                alphabet.lower()
                                wrong_guess.append(alphabet.lower())
                            except ValueError:
                                wrong_guess.append(alphabet)
                            attempt -= 1
                    else:
                        print('please input only one word')
                        count_guess += 1
                        attempt -= 1
                else:
                    count_guess += 1
                    wrong_guess.append(alphabet)
                    attempt -= 1
            else:
                print()
                create_question(word)
                print(f'     score {score}, remaining wrong guess {attempt}, wrong guessed: {guess}')
                print()
                print()
                score += (attempt * 2)
                print(f'congratulation you win this game with score {score} points')
                print()
                break
        elif attempt <= 0:
            print('over attempt ')
            break


def game():
    """
    game set in one round
    """
    print("Select Category:")
    print()
    print('1.Animal')
    print('2.Food')
    print()
    text = choose_catagory()
    words = openfile(text)
    word = rand_word(words)
    print(word[1])
    console(word)


def main():
    game()
    while True:
        ask = input('(p)lay again or (q)uit: ')
        if ask == 'q' or ask == 'Q':
            break
        elif ask == 'p' or ask == 'P':
            game()
        print()


if __name__ == '__main__':
    main()
