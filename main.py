def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_count = get_chars(text)
    print(f"---Begin report of {book_path} ---")
    print(f"{num_words} words found in the document \n")
    
    for entry, times in chars_count.items():
        print(f"The '{entry} character was found {times} times")
    print("--- End report ---")
def get_book_text(path):
    with open(path) as f:
        return f.read()  # Return the content of the file

def get_num_words(text):
    return len(text.split())  # Return the word count

def get_chars(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

main()
