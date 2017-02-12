import sys

levels = {'easy': 0, 'medium': 1, 'hard': 2}

blanks = ['__1__', '__2__', '__3__', '__4__']

easySentences = [
    'You can\'t __1__ an __2__ without __3__ a few __4__.',
    '__1__ your __2__ close and your __3__ __4__.',
    'The __1__ is always __2__ on the other __3__ of the __4__.',
    'If you __1__ something __2__ right, you have to __3__ it __4__.'
]

easySentencesAnswers = [['make', 'omelet', 'breaking', 'eggs'],
                        ['Keep', 'friends', 'enemies', 'closer'],
                        ['grass', 'greener', 'side', 'hill'],
                        ['want', 'done', 'do', 'yourself']]

mediumSentences = [
    'A __1__ of a thousand __2__ begins __3__ a __4__ step',
    'Don\'t __1__ off until __2__ what you __3__ do __4__',
    '__1__ for the __2__, prepare __3__ the __4__',
    'When the __1__ gets __2__, the __3__ get __4__'
]

mediumSentencesAnswers = [['journey', 'miles', 'with', 'single'],
                          ['put', 'tomorrow', 'can', 'today'],
                          ['Hope', 'best', 'for', 'worst'],
                          ['going', 'tough', 'tough', 'going']]

hardSentences = [
    'You can __1__ a horse to __2__, but you can\'t __3__ him __4__ it',
    'When __1__, think of __2__, but don\'t think of __3__ when you are __4__',
    'A __1__ thing may become a __2__ thing __3__ certain __4__. ',
    'It is when you are __1__ what you have __2__ from books that you __3__ you had __4__ more.'
]

hardSentencesAnswers = [['lead', 'water', 'make', 'drink'],
                        ['rich', 'poverty', 'riches', 'poor'],
                        ['bad', 'good', 'under', 'conditions'],
                        ['using', 'learned', 'wish', 'read']]

sentences = [easySentences, mediumSentences, hardSentences]
answers = [easySentencesAnswers, mediumSentencesAnswers, hardSentencesAnswers]

lives = 5


def select_difficulty():
    """Selects difficulty

    Takes an input from the user of easy, medium or hard
    and returns a corresponding index that is needed to 
    get the correct data from data lists.

    Returns:
        an integer index of levels dictionary
    """
    difficulty = ''
    while difficulty != 'easy' and difficulty != 'medium' and difficulty != 'hard':
        difficulty = raw_input('Please select your difficulty: easy, medium, hard: ')
    print 'You chose level: ', difficulty
    return levels[difficulty]


def start_game(difficulty):
    """Starts the game

    Starts the game given the difficulty integer.

    Args:
        difficulty: an integer key from dictionary levels
    """
    global sentences, answers, blanks
    correct_words = answers[difficulty]
    sentence = sentences[difficulty]

    for level in range(4):
        play_level(correct_words[level], blanks, sentence[level])
    print 'Congratulations you won the game!'


def play_level(correct_words, blanks, sentence):
    """Plays the level

    Loops through the 4 levels of the game.

    Args:
        correct_words: A list on which the user's input is checked upon.
        blanks: A list which corresponds to a blank of the sentence.
        sentence: The sentence which user should fill in the blank.
    """
    print sentence
    for index in range(4):
        check_word(correct_words[index], blanks[index])
        sentence = sentence.replace(blanks[index], correct_words[index])
        print sentence


def check_word(correct_word, blank):
    """Checks the users input

    Check if the user's given input is correct,
    if not, subtract one from his total lives
    and end the game if no more lives left.  

    Args:
        correct_word: A string on which the user's input is checked upon.
        blank: A string which corresponds to a blank of the sentence.
    """
    global lives
    word = raw_input('Fill in the blank ' + blank + ': ')
    while word != correct_word:
        lives -= 1
        if lives != 0:
            print 'That isn\'t the correct answer! Let\'s try again! You only have', lives, 'lives left.'
            word = raw_input('try again: ')
        else:
            print 'You have no lives left! The game is over'
            sys.exit()
    else:
        print '[------ Correct! ------]'


def main():
    """The main function.

    The main function that is called upon running the application.
    """
    global levels
    difficulty = select_difficulty()
    start_game(difficulty)


main()
