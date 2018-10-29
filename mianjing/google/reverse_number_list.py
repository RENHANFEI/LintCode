def reverse_numbers(nums):
    reverse_dict = {0:0, 1:1, 2:2, 5:5, 6:9, 9:6, 8:8}
    ans = []
    for num in nums:
        if num == 0:
            ans.append(num)
            continue

        if num % 10 == 0: 
            continue

        reverse = 0
        valid = True

        while num > 0:
            digit = num % 10
            if digit in reverse_dict:
                reverse = reverse * 10 + reverse_dict[digit]
                num //= 10
            else:
                valid = False
                break

        if valid:
            ans.append(reverse)

    return ans

test = [19, 61, 10, 0, 131, 22, 5]

print(reverse_numbers(test))


'''
* Reverse Digit: 
0 -> 0
1 -> 1
2 -> 2
3 -> None
4 -> None
5 -> 5
6 -> 9
7 -> None
8 -> 8
9 -> 6
* Reverse Order
10 -> 01? - assume invalid
131 -> None
151 -> 151
1521 - > 1251

negative?
'''

