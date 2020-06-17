'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here

    # k is the total number of elements in the sliding window
    # window moves 1 space at a time to the right so need a counter
    # to change start point of things
    # counter must stop at end of array length minus k 
    # place in temp list
    # check the max value in each list
    # in new list append max of the sliding amount

    new_list = []
    length = int(len(nums) - k)
    beginning = 0
    end = k
    counter = 0
    

    while counter  <= length:
        temp_list = nums[beginning:end]
        counter += 1
        beginning += 1
        end += 1
        print (temp_list)
        max_value = max((temp_list))
        new_list.append(max_value)

    return new_list






if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
