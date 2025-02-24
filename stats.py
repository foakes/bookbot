def get_wordcount(full_book_str):
    book_word_list = full_book_str.split()
    num_words = len(book_word_list)
    return num_words

def get_char_count(full_book_str):
    lowercased = full_book_str.lower()
    char_dict = {}
    for c in lowercased:
        if c not in char_dict:
            char_dict[c] = 0
        char_dict[c] += 1
    return char_dict

def sort_on(dict):
    for key in dict:
        return dict[key]

def generate_report_values(char_dict):
    dict_key_list = []
    for pair in char_dict:
        dict_key_list.append({pair : char_dict[pair]})
    dict_key_list.sort(reverse=True, key=sort_on)
    return dict_key_list
    


    
