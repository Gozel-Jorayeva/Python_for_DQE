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

# (?:^|\s)(.*?!)              ('([.!?]\s*)')
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

#
# print('\n')
# d = catch_error(hometask)
# a = normalize_letter_cases(hometask)
# b = create_new_sentence(a)
# c = count_text_spaces(b)
# print(b, '\n\n')
# print('Number of whitespace characters in this text is:', c, '\n\n')
