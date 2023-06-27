import time

# function to round the time to 2 decimal places


def round_down(num1):
    num1 = float(round(num1, 2))
    return num1


# function to calculate the gross words per minute


def gross_wpm():
    g_wpm = (len(user_sentence) / 9) / (round_down(timeC) / 60)
    g_wpm = float(round(g_wpm, 2))
    return g_wpm


# sentence variable
sentence = 'The quick brown fox jumps over the lazy dog'
# endless while loop
while True:
    # welcome statements
    name = input('Please enter your name: ').capitalize()
    print('Welcome', name)
    print('Copy the following sentence:')
    print(sentence)
    start = input('Hit the enter key to start: ')
    # if start = empty, then the user hit enter
    if start == '':
        # start a timer
        timeA = time.time()
        user_sentence = input('GO: ')
        timeB = time.time()
        # zip compares the 2 sentences
        a = zip(sentence, user_sentence)
        # list of correct characters
        correct = []
        # list of wrong characters
        wrong = []
        # compare each character with this for loop
        for i, j in a:
            if i == j:
                correct.append(j)
            else:
                wrong.append(j)
        timeC = timeB - timeA
        print('You took ', round_down(timeC), 'seconds.')
        print('The where ', len(wrong), 'error(s) found.')
        print('You gross WPM is: ', gross_wpm(), 'words per minute.')
        print('Try again.')
        print('')
