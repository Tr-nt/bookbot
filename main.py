#Function reads text from file and returns it as a string
def open_book():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

#Function returns list of words in text
def obtain_text(book_text):
    words = book_text.split()
    return words

#Function returns word count of text via length of list
def word_count(words):
    return len(words)

#Function returns letter count of words in text via dictionary with letter as key and count as value
def letter_count(words):
    letters = {}
    #Iterates through each word in list of words
    for word in words:    
        word = word.lower()
        #Iterates through each letter in word
        for letter in word:
            #If letter is in dictionary, increment value by 1
            if letter in letters and letter.isalpha():
                letters[letter] += 1
            #If letter is not in dictionary and is a letter, add letter to dictionary with value of 1
            elif letter.isalpha() and letter not in letters:
                letters[letter] = 1
    #sort the dictionary by key
    #Turns dictionary into a list of sorted tuples
    letters = dict(sorted(letters.items()))
    return letters

#Function returns sorted list of words in text
def sort_on(dict):
    return dict["num"]

#Function that returns list of sorted letters in dictionary
def list_letters(letters):
    #Turns dictionary into list of dictionaries
    letters_list = [{'letter': key , 'num': value} for key, value in letters.items()]

    #Sorts list of dictionaries by value
    letters_list.sort(reverse=True, key=sort_on)

    #Prints out list of dictionaries
    for i in range(0, len(letters_list)):
        print(f'The {letters_list[i]["letter"]} character was found {letters_list[i]["num"]} times')
    print("----End of Report----")

    #returned list for testing purposes
    #return letters_list

#Main function that calls all other functions
def main():
    book_text = open_book()
    words = obtain_text(book_text)
    alpha_count = letter_count(words)   
    report = list_letters(alpha_count)
    

if __name__ == "__main__":
    main()
