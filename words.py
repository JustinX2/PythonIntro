#Step Two: Starting On Your Own
#Do this work in a new file, words.py.

#For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!

#Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)

#Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).

#Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

#For example:

# this should print "HELLO", "HEY", "YO", and "YES"

#print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   #must_start_with={"h", "y"})

def print_upper_words(words, start_with=None):
    if start_with is not None:
        for word in words:
            print(word.upper())
    else:
        for letter in start_with:
            start_letters=letter.lower()
        for word in words:
            if word[0].lower() in start_letters:
                print(word.upper())
