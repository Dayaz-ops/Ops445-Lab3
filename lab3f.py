#!/usr/bin/env python3

# Initialize the list with the values 1, 2, 3, 4, 5
my_list = [1, 2, 3, 4, 5]

# Function to add a new item to the list by increasing the last item by 1
def add_item_to_list(ordered_list):
    last_item = ordered_list[-1]  # Get the last item
    ordered_list.append(last_item + 1)  # Append the next item to the list

# Function to remove specified items from the list
def remove_items_from_list(ordered_list, items_to_remove):
    for item in items_to_remove:
        if item in ordered_list:
            ordered_list.remove(item)  # Remove each item if found in the list

# Main code
if __name__ == '__main__':
    print(my_list)  # Print the original list
    add_item_to_list(my_list)  # Add new items to the list
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)  # Print the updated list
    remove_items_from_list(my_list, [1, 5, 6])  # Remove specified items
    print(my_list)  # Print the final list after removal
