def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """

    # YOUR CODE HERE 
    #take an arary of nums, set a start and stop
    for num in range(20, 40, 10):
      print(num, "fits")
   



in_range([10, 20, 30, 40, 50], 15, 30)            
