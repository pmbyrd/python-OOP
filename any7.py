def any7(nums):
    """Are any of these numbers a 7? (True/False)
    Pass in an array of numbers to check if a integar is 7
    """

    # YOUR CODE HERE
    if any(num == 7 for num in nums):
        return True
    else: 
        return False

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

