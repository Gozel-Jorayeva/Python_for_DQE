# # 4_3 homework
# 
# # 1. Copy text to variable called "hometask"
# hometask = """homEwork:
# 
#   tHis iz your homeWork, copy these Text to variable.
# 
# 
# 
#   You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
# 
# 
# 
#   it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
# 
# 
# 
#   last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""
# 
# import re
# 
# 
# def catch_error(t):
#     try:
#         if isinstance(t, list):
#             raise ValueError("List input is given\n\n")
#         else:
#             print('Right input\n\n')
#     except ValueError:
#         print("Wrong input\n\n")
# 
# 
# def normalize_letter_cases(text):
#     punc_filter = re.compile('([.!?]\s*)')
#     split_with_punctuation = punc_filter.split(text)
#     capitalize_first_letters = ''.join([i.capitalize() for i in split_with_punctuation])
#     fix_mistake = capitalize_first_letters.replace(" iz ", " is ")
#     return fix_mistake
# 
# 
# def create_new_sentence(word):
#     take_last_words = ' '.join(re.findall(r'\w+[.:]', word)).replace('.', '') + '.'
#     add_new_sentence = word[:241] + ' ' + take_last_words + word[241:]
#      punc_filter = re.compile('([.!?]\s*)')
#     split_with_punctuation = punc_filter.split(add_new_sentence)
#     capitalize_first_letters = ''.join([i.capitalize() for i in split_with_punctuation])
#     return capitalize_first_letters
# 
# 
# def count_text_spaces(space):
#     find_spaces = len(re.findall('\s+', space))
#     return find_spaces
# 
# print('\n')
# d = catch_error(hometask)
# a = normalize_letter_cases(hometask)
# b = create_new_sentence(a)
# c = count_text_spaces(b)
# print(b, '\n\n')
# print('Number of whitespace characters in this text is:', c, '\n\n')
# 
# 
# 
# 
# 
# 
# 
# import random
# import string
# 
# # dict_list = [{random.choice(string.ascii_lowercase): random.randint(0, 100) for i in range(random.randint(0, len(string.ascii_lowercase)))} for k in range(random.randint(2, 4))]
# # print(dict_list)
# 
# def create_list(d_count, key_values):
#     dict_list = []
#     for i in range(d_count):
#         d_key = [random.choice(string.ascii_lowercase) for i in range(key_values)]
#         d_value = [random.randint(0, 100) for k in range(key_values)]
#         rand_dict = {k: v for k, v in zip(d_key, d_value)}
#         dict_list.append(rand_dict)
#         d_count -= 1
#     return dict_list
# 
# 
# def choose_random_values(rand_num):
#     for i in rand_num:
#     result, dict_two = {}, {}
#         for key, value in i.items():
#             if key in dict_two:
#                 dict_two[key]['count'] += 1
#                 if dict_two[key]['value'] < value:
#                     dict_two[key]['value'] = value
#                     dict_two[key]['max_index'] = dict_two[key]['count']
#             else:
#                 dict_two[key] = {'value': value, 'count': 1, 'max_index': 1}
# 
# 
# def create_random_dict(d):
#     for k, v in dict_two.items():
#         value_count = v['count']
#         max_index = v['max_index']
#         if value_count == 1:
#             result_key = f'{k}'
#         else:
#             result_key = f'{k}_{max_index}'
#         result[result_key] = v['value']
#     return result
# 
# r_value = create_list(3, 2)
# r_dict = choose_random_values(r_value)
# print(r_dict)
# 
# 











# 4_3 homework

# 1. Copy text to variable called "hometask"
hometask = """homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

import re


def catch_error(t):
    try:
        if isinstance(t, list):
            raise ValueError("List input is given\n\n")
        else:
            print('Right input\n\n')
    except ValueError:
        print("Wrong input\n\n")

def normalize_letter_cases(text):
    punc_filter = re.compile('([.!?]\s*)')
    split_with_punctuation = punc_filter.split(text)
    capitalize_first_letters = ''.join([i.capitalize() for i in split_with_punctuation])
    fix_mistake = capitalize_first_letters.replace(" iz ", " is ")
    return fix_mistake

def create_new_sentence(word):
    take_last_words = ' '.join(re.findall(r'\w+[.]', word)).replace('.', '') + '.'
    add_new_sentence = word[:241] + ' ' + take_last_words + word[241:]
    punc_filter = re.compile('([.!?]\s*)')
    split_with_punctuation = punc_filter.split(add_new_sentence)
    capitalize_first_letters = ''.join([i.capitalize() for i in split_with_punctuation])
    return capitalize_first_letters


def count_text_spaces(space):
    find_spaces = len(re.findall('\s+', space))
    return find_spaces


print('\n')
d = catch_error(hometask)
a = normalize_letter_cases(hometask)
b = create_new_sentence(a)
c = count_text_spaces(b)
print(b, '\n\n')
print('Number of whitespace characters in this text is:', c, '\n\n')




# ====================================================================================================================
import random
import string

# dict_list = [{random.choice(string.ascii_lowercase): random.randint(0, 100) for i in range(random.randint(0, len(string.ascii_lowercase)))} for k in range(random.randint(2, 4))]
# print(dict_list)

def create_list(d_count, key_values):
    dict_list = []
    for i in range(d_count):
        d_key = [random.choice(string.ascii_lowercase) for i in range(key_values)]
        d_value = [random.randint(0, 100) for k in range(key_values)]
        rand_dict = {k: v for k, v in zip(d_key, d_value)}
        dict_list.append(rand_dict)
        d_count -= 1
    return dict_list



def choose_random_values(rand_num):
    result, dict_two = {}, {}
    for i in rand_num:
        for key, value in i.items():
            if key in dict_two:
                dict_two[key]['count'] += 1
                if dict_two[key]['value'] < value:
                    dict_two[key]['value'] = value
                    dict_two[key]['max_index'] = dict_two[key]['count']
            else:
                dict_two[key] = {'value': value, 'count': 1, 'max_index': 1}

    for k, v in dict_two.items():
        value_count = v['count']
        max_index = v['max_index']
        if value_count == 1:
            result_key = f'{k}'
        else:
            result_key = f'{k}_{max_index}'
        result[result_key] = v['value']
    return result

a = create_list(3, 2)
b = choose_random_values(a)
print(b)



