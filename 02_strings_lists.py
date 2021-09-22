# strings, lists, and tuples

#strings
course_code = 'CSCI 1030U'
course_name = 'Introduction to CS'
course_code_and_name = f'{course_code} - {course_name}'
price = 8.99
customer_message = f'The price of the item is ${price} plus tax'

print(course_code[9]) #last character (fragile method - any change to the course_code breaks)
print(course_code[len(course_code)-1]) #last character (robust method)
print(course_code[-1]) #last character (Python shortcut)
# print(course_code[10]) #runtime error

# substrings  using the slice operator [start:stop:step]
print(customer_message[0:len(customer_message):2])
print(customer_message[::-1])


# programming exercise - simplified version (for practice - just reverse the long way)
first_name = 'Lorenzo'
reverse_first_name = ''
for i in first_name:
    # print(i, end='')
    reverse_first_name = i+reverse_first_name 
print(reverse_first_name)


print(course_code_and_name)

reverse_fn = ''
for index in range(len(first_name) -1,-1,-1):
    reverse_fn = reverse_fn + first_name[index]
print(reverse_fn)

    




#lists
numbers = [0,1,2,3,4,5]
test_marks = [15.0, 14.0, 11.0, 9.5, 2.5, 14.0, 13.5]
student_names = ['Barbara', 'Lucy', 'Kumar', 'Steve']

print(student_names[len(student_names)-1])
print(student_names[-1])



#coding exercise
sentence = 'the quick brown fox jumped over the lazy dog'
sentence_reverse = ''
#expected output: '
word  = ''
# 1. divide the string into a list of words
list_of_words = []
for character in sentence:
    if character == ' ':
        list_of_words.append(word)
        word = ''
    else:
        word = word + character
        # not the end of a word
# 2. reverse the list of words ([::-1]
for i in range(len(list_of_words) -1,-1,-1):
    sentence_reverse = sentence_reverse + list_of_words[i] + ' '
print(sentence_reverse)
# 3. combine the word list into a single string (spaces in between)

