def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    num_words = len(text.split())
    return num_words

def lower_case(text): 
    lower_text = text.lower()
    return lower_text

def character_count(lower_text):
    char_count = {}
    for char in lower_text:
        # 1. Check if the character is already a key in the dictionary
        if char in char_count:
            # 2. If it is, increment its current count
            char_count[char] += 1
        else:
            # 3. If it's new, add it to the dictionary with a count of 1
            char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

    








    
    
