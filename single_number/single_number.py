'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # sort array
    # check if item in spot before or after is the same as item you are on
    # if not then return item

    arr.sort()
    length = len(arr)

    prev_location = 0
    current_location = 0
    next_location = 1
    found_number = None
    Found = False
    print(arr)
    for i, current_location in enumerate(arr):
        if i == 0:
            print(i)
            pass
        elif i == (length - 1) and not Found:
            if prev_location != current_location:
                found_number = current_location


        else:
            prev_location = arr[i - 1] 
            
            if not Found:
                next_location = arr[i + 1]
                print(f"Current Location{current_location}, Previous {prev_location}, Next{next_location}")
                if prev_location == current_location or current_location == next_location:
                    pass
                else:
                    found_number = current_location
                    Found = True
                # if prev_location != current_location:
                

    return found_number





if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 9, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
    