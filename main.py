import sys
from stats import get_book_text
from stats import count_words
from stats import lower_case
from stats import character_count
from stats import sort_on

#required arguments to run code
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

print(sys.argv)

# first arugment or arg[0] is the name of the program "main.py"
path = sys.argv[1]



def main():
    book_path = get_book_text(path)
    text = book_path
    num_words = count_words(text)
    lower_text = lower_case(text)
    char_count = character_count(lower_text)
    sorted_list = []
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path} ...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for ch in char_count:
        sorted_list.append({"char": ch, "num": char_count[ch]})
    sorted_list.sort(reverse=True, key=sort_on)

    for item in sorted_list:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")
        continue 
    print("============= END ===============")
  
main()
 
