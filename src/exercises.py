def reverse_list(input_list):
    lis=input_list[::-1]
    return lis

def count_digits(number):
    c=0
    for i in str(number):
        c=c+1
    return c