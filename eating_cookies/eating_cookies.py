'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    # cookies come in with n
    # capacity is n
    # need to see with values of 1 2 or 3 total to n



    # 5
    # 1,1,1,1,1
    # 1,1,1,2
    # 1,1,3
    # 1,2,2
    # 1,3,1
    # 2,3
    # 3,2
    # 2,2,1
    # 2,1,2
    # 3,1,1
    # 2,1,1,1

    if n == 0:
        return 1
    elif n < 0:
        return 0

    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
