def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
<<<<<<< HEAD
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max
=======
    max_number = 0
    for i in numbers:
        if i > max_number :
            max_number = i
        return max_number    
>>>>>>> dfa3f42d1ceb08cacca4df4e32604c9cd46b18e9


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
