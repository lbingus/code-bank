# gives the text 'Hello world' in console
print('Hello world')

"""
This is a 
multi line
comment!
"""

# if " is surrounded by ', then " will be printed
print('"Now"')

"""
this does not work the other way around
" always has to be present in an even number
gotta include \ if you want to print '''
\ does not represent the start/end of a string
but only used to escape the '' around it
\ can be used for e.g. unicode characters
"""
print('\'')
print('\"')
print('This says \'Python\'')
print('-\n-') # \n indicates a new line for printed output (not printed itself)
print('-\r-') # \r indicates end of line but starts line new
print('-\t-') # \t for tabulator (4 spaces width)
print('\\') # shows one \

print('Today is Monday, \nthe sun is shining '
      'and someone shouted "Morning!"')

print(13)
print(12 + 1) # spaces at the end no problem

print('Hallo' + ' ' + 'Leute') # +  concatenates strings

x = 12 + 1
print(x)

x = x - 5
print(x)

"""
variables are not bound to specific variable type (e.g. like integers or
strings). always use variable names that say what they contain to avoid
mistakes or confusions
"""

greeting = 'Heyaaa'
print(greeting)

num = 12_345_678_901_234_567
print(num)

# end of lesson: 16/05/2022 15:35