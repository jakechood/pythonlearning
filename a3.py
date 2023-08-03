"""A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
"""
wordlist = []
board = []
cstrlist = []
rstrlist = []
wordlist = ['HAVE', 'HOLD', 'RUN', 'BOLD']
wordfile = str(['HAVE/n', 'HOLD/n', 'RUN/n', 'BOLD/n'])
board = [['H', 'R', 'U', 'N', 'H'], ['O', 'A', 'L', 'O', 'A'], ['L', 'O', 'V', 'R', 'E'], ['D', 'L', 'H', 'E', 'A'], ['H', 'B', 'O', 'L', 'D']]
boardfile = str(['HRUNH/n', 'OALOA/n', 'LOVRE/n', 'DLHEA/n', 'HBOLD/n'])

def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    """
    i = 0
    while i < len(wordlist):
        return word in wordlist
        i = i + 1

def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    """
    rstrlist = ''
    i = row_index
    for char in board[i]:
        rstrlist = rstrlist + char
    return rstrlist


def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    """
    cstrlist = ''
    i = column_index
    for char in board:
        cstrlist = cstrlist + (char[i])
    return  cstrlist


def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    """

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True
    return False


def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    """
    i = 0
    while i < len(board[0]):
        if word in make_str_from_column(board, i):
            return True
        i = i + 1
    return False

def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    """
    blob = ''
    for word in range(len(board)):
        if blob in make_str_from_row(board, word):
            return True
    if board_contains_word_in_column(board, word) or board_contains_word_in_row(board, word):
            return True
    return False

def word_score(word):
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('DRUDGERY')
    16
    """
    i = len(word)
    if i < 3:
        return i * 0
    elif 3 <= i <= 6:
        return i * 1
    elif 7 <= i <= 9:
        return i * 2
    elif i >= 10:
        return i * 3
    return i


def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    """
    pscore = player_info[1]
    score = pscore + word_score(word)
    player_info[1] = score

def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    """
    numword = 0
    for word in words:
        if board_contains_word(board, word):
            numword = numword + 1
    return numword

def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """
    listy = []
    word = ''
    for line in words_file:
        for char in line:
            if char != '/n':
                word = word + char
        listy.append(word)
    return listy

def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    """
    listy = []
    for line in board_file:
        sub = []
        for char in line:
            if char != '/n':
                sub.append(char)
        if sub != []:
            listy.append[sub]
    return listy