def output_time(time, length):
    """
    This function changes the output of expectedTime(), which
    is normally in seconds, to a unit that is much more
    understandable. This includes, minutes, hours, days,
    months, years, and centuries.
    """

    SECOND = 1
    MINUTE = 60 * SECOND
    HOUR = 60 * MINUTE
    DAY = 24 * HOUR
    MONTH = 365/12 * DAY
    YEAR = 12 * MONTH
    CENTURY = 100 * YEAR

    if time >= CENTURY:
        divisor = CENTURY
        unit = "centuries"
    elif time >= YEAR:
        divisor = YEAR
        unit = "years"
    elif time >= MONTH:
        divisor = MONTH
        unit = "months"
    elif time >= DAY:
        divisor = DAY
        unit = "days"
    elif time >= HOUR:
        divisor = HOUR
        unit = "hours"
    elif time >= MINUTE:
        divisor = MINUTE
        unit = "minutes"
    elif time >= SECOND:
        divisor = SECOND
        unit = "seconds"
    else:
        return

    print "{0:0>2}:\t{1:f}\t{2}".format(length, time/divisor, unit)


def expectedTime(size, type):
    """
    This function outputs the expected time to guess
    a password based on a specified length and type.
    The parameters for the function are:
        length		any positive integer
        type		dice, cards, dictionary

    The three types correspond to where the "characters"
    of the password come from. "dice" will generate a
    password using 6-sided die. "cards" will generate a
    password using 52 cards from a deck, with no repeats.
    "dictionary" will assume a dictionary size of 200,000
    words.
    """

    # Initialize sizes
    dice = 6  # Number of sides on dice
    cards = 52  # Number of cards in deck
    dictionary = 200000  # Number of words in dictionary
    keyboard = 96  # Number of keys on keyboard
    guesses = 100000000000  # Per second (super computer)
    time = None

    # Determine type of generation
    if type == "dice":
        time = ((dice ** size) * 0.5) / guesses
    
    elif type == "cards":
        space = 1
        x = 0
        while (x < size):
            space = space * (cards - x) 
            x = x + 1
        time = (space * 0.5) / guesses

    elif type =="dictionary":
        time = ((dictionary ** size) * 0.5) / guesses

    elif type == "character":
        time = ((keyboard ** size) * 0.5) / guesses

    else:
        print "Incorrect type. Please try again."

    if time:
        output_time(time, size)


def main():
    """
    This is the main method of the script that will run
    upon execution.
    """

    print "------------------------------------------"
    print "Program to determine the expected time to "
    print "crack passwords of various lengths. Any   "
    print "time less than 1 second is not displayed. "
    print "------------------------------------------"

    print "\n------------------------------------------"
    print "Expected Time for 6-sided dice:"
    print "------------------------------------------"
    for x in range(1, 28):
        expectedTime(x, "dice")

    print "\n------------------------------------------"
    print "Expected Time for 52-card deck:"
    print "------------------------------------------"
    for x in range(1, 14):
        expectedTime(x, "cards")
    
    print "\n------------------------------------------"
    print "Expected Time for 96-key keyboard:"
    print "------------------------------------------"
    for x in range(1, 12):
        expectedTime(x, "character")

    print "\n------------------------------------------"
    print "Expected Time for 200,000 word dictionary:"
    print "------------------------------------------"
    for x in range(1, 5):
        expectedTime(x, "dictionary")


if  __name__ == '__main__':
    main()