def count_words(book):
    """Prompts the user for a keyword and returns the occurance count."""
    try:
        with open(book, encoding='utf-8') as file_object:
            contents = file_object.read()
            while True:
                x = 0
                word_lookup = input("What word would you like counted? 'r' to restart. ")
                if word_lookup == 'r':
                    print("\tProgram restarted.")
                    break
                else:
                    for word in contents.split(): #this splits each word into an item on in a list
                        if word.lower() == word_lookup.lower(): #this makes the search case insensitive
                            x += 1 #adds to the counter
                print(f"\tThe word '{word_lookup}' appears {x} times in file '{book}'.")
    except FileNotFoundError:
        print(f"\nFile ({book}) not found.") #Write 'pass' to silently ignore the error

print("For example: 'alice' 'bible' 'lotr'\n") #
while True:
    book_title = input("What's the title of your book? 'q' to quit: ")
    if book_title == 'q':
        print("\tProgram ended.")
        break
    else:
        count_words(f'text_files/{book_title}.txt')
