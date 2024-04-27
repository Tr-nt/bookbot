def open_book():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def obtain_text(book_text):
    words = book_text.split()
    return words

def word_count(words):
    return len(words)

def letter_count(words):
    letters = {}

    for word in words:    
        word = word.lower()
        for letter in word:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    #sort the dictionary by key
    letters = sorted(letters.items())
    return letters




def main():
    book_text = open_book()
    words = obtain_text(book_text)
    print(word_count(words))
    print(letter_count(words))


if __name__ == "__main__":
    main()
