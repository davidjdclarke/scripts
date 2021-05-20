import numpy as np

def score_probability(statement):
    """
    This function returns true or false depending on what percentage of the elements in the input
    array match the key words dictated by the local variable "key_words". 

    If more than 70% of elements in statements match the key words, functions returns True, else
    the function return False.

    Input(s): 
    statement --> list[string]
    Output(s): 
    Boolean
    """
    # Set key Words
    key_words = ['age', 'year', 'born', 'date of birth'] 

    # Zero word counts
    words_total = 0
    occurences = 0 

    # You could also just set words_total as:
    # words_total = len(statement) 

    # Iterate over elements in statement
    for word in statement:
        words_total += 1 # incerement total words
        if word in key_words: # check if word in key_words
            occurences += 1 # if so, increment occurences
    return (occurences / words_total) > 0.7 # return true if 70% of all words are key_words


def is_ordered1(numbers):
    """
    Returns True, if and only if the elements of the input array numbers are ordered from smallest to largest:

    Input(s):
    numbers --> list[int]

    Output(s):
    boolean
    """
    # Each index larger than or equal to the one before
    return True == all([numbers[i] <= numbers[i+1] for i in range(len(numbers)-1)])

def is_ordered2(numbers):
    """
    Returns True, if and only if the elements of the input array numbers are ordered from smallest to largest:

    Input(s):
    numbers --> list[int]

    Output(s):
    boolean
    """
    # Use Recursion
    if len(numbers) > 2:
        return numbers[0] <= numbers[1] and is_ordered2(numbers[1:])
    else:
        return numbers[0] <= numbers[1]

def is_ordered3(numbers):
    """
    Returns True, if and only if the elements of the input array numbers are ordered from smallest to largest:

    Input(s):
    numbers --> list[int]

    Output(s):
    boolean
    """
    # Use Numpy
    return np.all(np.diff(numbers) >= 0)

def main():
    print(is_ordered3([1, 1, 1, 1]))
    print(is_ordered3([1, 2, 3]))
    print(is_ordered3([7, -4, 8, 12]))

if __name__ == "__main__":
    main()