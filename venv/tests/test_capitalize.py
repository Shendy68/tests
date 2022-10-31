from main.capitalize import capitalize


if capitalize('hello') != 'Hello':
    raise Exception('Function work incorrect!')


if capitalize('') != '':
    raise Exception('Function work incorrect!')


print('All tests sucesfully complete!')