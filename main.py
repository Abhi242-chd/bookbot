from stats import *
import sys

def main():
    if len(sys.argv) == 2:
        book_loc = f"{sys.argv[1]}"
        text = get_book_text(book_loc)
        char_dir = count_char(text)
        print("============ BOOKBOT ============")
        print(f"Analying book found at {book_loc}")
        print("----------- Word Count ----------")
        print(count_words(text))
        print("--------- Character Count -------")
        for char in char_dir:
            print(f"{char['chr']}: {sort_on(char)}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()

