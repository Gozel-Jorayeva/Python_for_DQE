# 4_3 homework
import re

# 1. Copy text to variable called "hometask"
hometask = """homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# print(hometask)
# create function called normalize_func with one argument
def normalize_func(h_text):
    # normalizing letter cases
    normalize_text = '. '.join(map(lambda s: s.capitalize(), h_text.split('.')))
    # fix mistake
    fix_mistake = normalize_text.replace(" iz ", " is ")
    # taking all last words of the sentences and removing dots and adding dot at the end of the sentence
    create_new_sentence = ' '.join(re.findall(r'\w+[.:]', fix_mistake)).replace('.', '') + '.'
    # adding new created sentence to the middle of the text
    new_text = fix_mistake[:244] + create_new_sentence + fix_mistake[244:]
    # printing count of the space/whitespace characters
    print('\nWhitespace/space characters number is:', len(re.findall('\s+', new_text)), '\n')
    # returning new created text
    return new_text
# calling function and showing the text we want to normalize
print('\n\n\nFirst function for normalizing text')
print(normalize_func(hometask))
print('\n\n\n\n\nSecond function for choosing random values')





# 4_2 homework
import random
import string

dict_list = [{random.choice(string.ascii_lowercase): random.randint(0, 100) for i in range(random.randint(0, len(string.ascii_lowercase)))} for k in range(random.randint(2, 4))]
# print(dict_list)
#
# creating function with one argument
def choose_random_values(rand_num):
    # creating two dictionaries
    result, dict_two = {}, {}
    # for each iteration in the given argument/list
    for i in rand_num:
        for key, value in i.items():
            if key in dict_two:
                dict_two[key]['count'] += 1
                if dict_two[key]['value'] < value:
                    max_index = dict_two[key]['max_index']
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
print(choose_random_values(dict_list))
