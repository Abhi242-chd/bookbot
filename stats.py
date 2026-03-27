def get_book_text(PATH):
    with open(PATH, encoding="utf-8") as f:
        return f.read()

def count_words(book):
    words = book.split()
    num_words = len(words)
    return f"Found {num_words} total words"

def sort_on(char_dir):
    return char_dir["num"]

	
def count_char(book):
    words = book.lower()
    char_dir = {}
    for char in words:
        if char.isalpha():
            char_dir[char] = char_dir.get(char, 0) + 1
    char_dir = get_dicts_list(char_dir)
    char_dir.sort(reverse=True, key=sort_on)
    return char_dir
    

def get_dicts_list(char_dir):
    up_char_dir = []
    for char in char_dir:
        char_dicts = {}
        char_dicts["chr"] = char
        char_dicts["num"] = char_dir[char]
        up_char_dir.append(char_dicts)
    return up_char_dir

