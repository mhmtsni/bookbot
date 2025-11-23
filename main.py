from stats import count_words, count_unique_characters, sort_unique_characters
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
        
def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    pathname = sys.argv[1]
    content = get_book_text(pathname)
    count_words(contents=content)
    count = count_unique_characters(content)
    sorted_list = sort_unique_characters(count)
    for object in sorted_list:
        print(f"{object["char"]}: {object["num"]}")
main()