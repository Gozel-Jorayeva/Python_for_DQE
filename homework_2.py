import random
import string

# create empty list and call it "dictList"
dict_list = []
# for each iteration create random number of dictionaries (randint from random library)
for i in range(random.randint(2,10)):
    # create random dictionary size and assign it to "size" variable
    size = random.randint(2,4)
    # create random letters for keys (using string library's ascii_lowercase method)
    keys = random.sample(string.ascii_lowercase,size)
    # create random numbers from 0 to 100 assign it to "values" variable
    values = (random.randint(0,100)
    # for each dict which are inside of list
    for i in range(size))
    # convert to key-value pairs
    dictionary = dict(zip(keys,values))
    # add created dictionaries to "dict_list"
    dict_list.append(dictionary)

print(dict_list)

# create new empty dictionary
dict_two = {}
# for each element in the above created "dict_list"
for i in dict_list:
    # for each key-value in "dict_list"
    for key, value in i.items():
        # if key is in dictionary ("dict_two")
        if key in dict_two:
            # increment the value
            dict_two[key]['count'] += 1
            # if key's value is less than value
            if dict_two[key]['value'] < value:
                # assign to "max_index" variable that here will be max indexes
                max_index = dict_two[key]['max_index']
                # key's value is equal to value
                dict_two[key]['value'] = value
                # max_index is assigned to key_count
                dict_two[key]['max_index'] = dict_two[key]['count']
        # else/in other case
        else:
            # write in "dict_two" key with value, count, max_index
            dict_two[key] = {'value': value, 'count': 1, 'max_index': 1}

# create new dictionary for the last results
result = {}

# for each key-value in "dict_two"
for key, value in dict_two.items():
    # assign to "value_count" variable the value
    value_count = value['count']
    # assign to "max_index" variable the maximum value
    max_index = value['max_index']
    # *if count is equal to one
    if value_count == 1:
        # f-string provide a convenient way to insert python expressions inside string literals for formatting.
        # then write the result as it is
        result_key = f'{key}'
    # else:
    else:
        # write in this format "key_underscore_max-index"
        result_key = f'{key}_{max_index}'
    # result of result_key with value add to "result" dictionary
    result[result_key] = value['value']

# print(dict_two)
# print the last output with the random dictionary key-value pairs and with renamed key with max value
print(result)



