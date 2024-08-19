def plusMinus(er):
    # Counters for positive, negative, and zero elements
    pos = 0
    neg = 0
    zero = 0
    
    # Iterate over each element in the array
    for i in er:
        if i < 0:
            neg += 1
        elif i == 0:
            zero += 1
        else:
            pos += 1

    # Calculate the ratios
    total = len(er)
    pos_ratio = pos / total
    neg_ratio = neg / total
    zero_ratio = zero / total

    return f"{pos_ratio:.6f}", f"{neg_ratio:.6f}", f"{zero_ratio:.6f}"

# Test the function
pos, neg, zero = plusMinus([-4 ,3, -9, 0, 4, 1])
print(pos)
print(neg)
print(zero)
