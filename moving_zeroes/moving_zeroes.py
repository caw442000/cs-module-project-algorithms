'''
Input: a List of integers
Returns: a List of integers
'''
# def moving_zeroes(arr):
#     # Your code here
#     for i in arr:
#         if arr[i] == 0:
#             arr.append(arr.pop(i))
#             print(i)


#     return arr

def moving_zeroes(arr):
    count = 0
    length_of_array = len(arr)

    

    for i in range(length_of_array):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < length_of_array:
        arr[count] = 0
        count += 1

    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 1, 0, -2, 0, 0]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")