def count_words(book):
    """Prompts the user for a keyword and returns the occurance count."""
    try:
        with open(book, encoding='utf-8') as file_object:
            contents = file_object.read().lower()
            
            while True:
                word_lookup = input("What word would you like counted? 'r' to restart. ").lower()
                if word_lookup == 'r':
                    print("\tProgram restarted.")
                    break
                print(f"\tThe word '{word_lookup}' appears {contents.split().count(word_lookup)} times in file '{book}'.")
    except FileNotFoundError:
        print(f"File ({book}) not found.")   #Write 'pass' to silently ignore error

print("For example: 'alice' 'bible' 'lotr'\n")
while True:
    book_title = input("What's the title of your book? 'q' to quit: ")
    if book_title == 'q':
        print("\tProgram ended.")
        break
    else:
        count_words(f'text_files/{book_title}.txt')
