# Author: MOG 11/15/21

my_string = input("Please input a list of numbers not seperated by anything: ")

my_list = list(my_string)
sorted_list = my_list.copy()
sorted_list.sort()

if sorted_list == my_list:
    print("This list is sorted.")
else:
    print("This list is not sorted.")