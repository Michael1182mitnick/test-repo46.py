# Write a Python program to remove duplicates from a list.

data = [10, 20, 30, 30, 40, 50, 50, 60, 80, 90]


def remove_duplicates(duplist):

    empyt_duplicate_list = []

    for elements in duplist:
        if elements not in empyt_duplicate_list:
            empyt_duplicate_list.append(elements)

    return empyt_duplicate_list


print(remove_duplicates(data))
