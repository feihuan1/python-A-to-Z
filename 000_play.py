def func(num1, num2):
    length = len(num1) + len(num2)

    big = 0
    small = 0

    j = 0
    k = 0
    while j < len(num1) and k < len(num2): 
        if j + k >= length/2 + 1:
            break
        if num1[j] > num2[k]:
            if num1[j] > big:
                big = num1[j]
                j+=1
            if num2[k] > small:
                small = num2[k]
                k+=1
        else:
            if num2[k] > big:
                big = num2[k] 
                k += 1
            if num1[j] > small:
                small = num1[j]
                j+=1
        print(j,k,big, small)



res = func([1,2], [3,4])
print(res)