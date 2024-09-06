'''
Write a python program to input integer values until a 0 is entered.
For each input integer if its odd, store in a dictionary under the key 'odd' 
and if its even, store in a dictionary under the key 'even'.

After a zero is entered, print the dictionary.

For example, if the input is:
2 3 5 4 6 0 

The output should be:
{'odd': [3, 5], 'even': [2, 4, 6]}
'''

value = int(input())
int_dict = {'odd': [], 'even': []}
i = 1
while i == 1:
    value = int(input("Input: "))
    if value == 0:
        print(int_dict)
        i = 0
    elif value % 2 == 1:
        int_dict['odd'].append(value)
    else:
        int_dict['even'].append(value)