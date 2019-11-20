import time

def find_longest_string(list_of_strings):
    longest_string = None
    longest_string_len = 0 
    for s in list_of_strings:
        if len(s) > longest_string_len:
            longest_string_len = len(s)
            longest_string = s
    return longest_string

list_of_strings = ['abc', 'python', 'dima']
print(find_longest_string(list_of_strings))

print(time.process_time())