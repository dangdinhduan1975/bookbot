import sys 
from stats import get_num_words, get_num_chars,sorted_char_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    content = get_book_text(sys.argv[1])
    word_count = get_num_words(content)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_stats = sorted_char_dict(get_num_chars(content))
    for stat in char_stats:
        if stat["name"].isalpha():
            print(f"{stat["name"]}: {stat["num"]}")
    print("============= END ===============")

main()