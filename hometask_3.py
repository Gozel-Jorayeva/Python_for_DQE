# importing regular expressions' library
import re

# 1. Copy text to variable called "hometask"
hometask = """homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# print(hometask)

# 2. Normalize the text's letter cases
# strip() method removes spaces from left&right sides.
# capitalize() first letter of string and make other letters lowercase
# split() the string at the dot seperator
text = '. '.join(map(lambda s: s.strip().capitalize(), hometask.split('.')))
# print(text)


# 3. Create one more sentence combining the last words of each sentence
# ' ' means, should be space between words
# join will return the words together in one line
# re means, regex. Find all words (\w+) near the dot . or colon :
sentence = ' '.join(re.findall(r'\w+[.:]', text))
# replaced dot with space
rep_dot = sentence.replace('.', '')
# string concatenation using join() method
# new_text = "".join([text, rep_dot])
#  format function is used here to combine the string
new_sentence = "{}{}".format(text, rep_dot)
# print(new_text)

# 4. Fix misspelling
# replaced iz to is
new_sentence = new_sentence.replace('iz', 'is')
print(new_sentence)

# 5. Count spaces and whitespaces
new_text = len(re.findall('\s+\n| +', new_sentence))
print(new_text)

# count() method returns the number of times the empty ' ' element appears
# new_sentence.count(' ')


