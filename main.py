def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    char_dict = check_alpha(text)
    chars_sorted = char_sorted(char_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f'{count_words(text)} words found in the document \n')
    for item in chars_sorted:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

def sort_on(d):
    return d["num"]

def char_sorted(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({'char': char, 'num': num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)
    
def count_char(text):
    chars = {}
    for word in text:
        lowered = word.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def check_alpha(text):
    chars = {}
    for word in text:
        lowered = word.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars
main()
