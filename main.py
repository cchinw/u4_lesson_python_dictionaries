def list_keys(dictionary):
    # Should return all keys in provided dictionary
    for key in dictionary:
        return dictionary[key]


def list_values(dictionary):
    # Should return all values in dictionary in a list
    dict = [dictionary[key] for key in dictionary]
    return dict


def update_dict(dictionary):
    # Should update the provided dictionary with the following properties => {"location":"Budapest", "year":"1989"}
    dictionary.update({"location": "Budapest", "year": "1989"})
    return


def access_dict(dictionary):
    # Should return the value of the dictionaries "age" key.
    return


def build_dict():
    # Build Your Own Dictionary using the constructor or curly bracket syntax
    my_dict = {
        'name': 'Lekan',
        'age': 40,
        'company': 'Facebook'
    }
    return my_dict


my_dict = {
    'name': 'Lekan',
    'age': 40,
    'company': 'Facebook'
}
my_dict2 = {
    'name': 'Chinwendu',
    'age': 38,
    'company': 'Google'
}
my_dict['job_title'] = 'Engineering Manager'
my_dict.update({'job_title': "SVP of Engineering"})
my_dict.update({'promotion': "CEO, Google"})
my_dict.update(my_dict2)
for key in my_dict:
    print(my_dict[key])
wgcddne = [my_dict[key] for key in my_dict]
print(wgcddne)
# print(my_dict)
