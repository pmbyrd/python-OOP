def print_upper_words(words, must_start_with):
    """Takes in a list of words and converts them into uppercase 
    A second parameter filters the words to be converted
    """

    for word in words:
        
        print(word.upper())



#starter value from example
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
    must_start_with={"h", "y"})

print_upper_words(["engery", "amazing", "everybody", "everywhere", "nowhere"],
    must_start_with={"e", "a"})