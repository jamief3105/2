
def max_min(numbers):
    #set first number in arry as max and min
    max_num = numbers[0] 
    min_num = numbers[0]
    # sort through rest of numbers in array, checking to see if each numbers is smaller than current min_num
    # or larger than current max_num.
    for i in range(1,len(numbers)):
        if numbers[i]>max_num:
            max_num = numbers[i]
        elif numbers[i] < min_num:
            min_num = numbers[i]
        else:
            continue
    return [min_num,max_num]
