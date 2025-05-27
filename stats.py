def get_num_words(document):
    word_list = document.split()
    count = len(word_list)
    return count


def get_num_chars(document):
    word_list = document.split()
    char_collection = {}
    for word in word_list:
        for char in word:
            if char.lower() in char_collection:
                char_collection[char.lower()] += 1
            else:
                char_collection[char.lower()] = 1
    return char_collection

def sort_on(dict):
    return dict["num"]

def sorted_char_dict(char_collection):
    list_of_dict = []
    for key, value in char_collection.items():
        char_dict = {}
        char_dict["name"] = key
        char_dict["num"] = value
        list_of_dict.append(char_dict)
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict
