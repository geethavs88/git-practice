def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    max_number = 0
    for i in numbers:
        if i > max_number :
            max_number = i
        return max_number    


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
