#!/usr/bin/env python3

# Global list 'my_list'
my_list = [100, 200, 300, 'six hundred']

def give_list():
    # Returns all of items in the global object my_list unchanged
    return my_list

def give_first_item():
    # Returns the first item in the global object my_list as a string
    return str(my_list[0])

def give_first_and_last_item():
    # Returns a list that includes the first and last items in the global object my_list
    return [my_list[0], my_list[-1]]

def give_second_and_third_item():
    # Returns a list that includes the second and third items in the global object my_list
    return [my_list[1], my_list[2]]

if __name__ == '__main__':
    # Main block
    print(give_list())  # Will print the entire list
    print(give_first_item())  # Will print the first item as a string
    print(give_first_and_last_item())  # Will print a list with the first and last items
    print(give_second_and_third_item())  # Will print a list with the second and third items
