'''
Write a function that takes arraylists of integers, A and B, 
and returns A_prime and B_prime, 
such that A_prime contains all elements of A that are not present in B 
AND B_prime contains all elements of B that are not present in A.

Example:

A: <4, 2, 6, 5, 2, 7, 2>
B: <3, 9, 2, 7, 1>

A_prime: <4, 6, 5, 2, 2>
B_prime: <3, 9, 1>


Use only one extra data structure to solve this.

Follow Up:
What if the two arrays are sorted?
'''

# time: O(M + N), space: O(M + N)
def get_prime(A, B):
    int_nums = dict()

    for a in A:
        if a in int_nums:
            int_nums[a] += 1
        else:
            int_nums[a] = 1

    for b in B:
        if b in int_nums:
            int_nums[b] -= 1
        else:
            int_nums[b] = -1

    A_prime, B_prime = [], []
    for val, num in int_nums.items():
        if num > 0:
            A_prime.extend([val] * num)
        if num < 0:
            B_prime.extend([val] * (-num))

    return A_prime, B_prime


'''
A: 2,2,2,4,5,6,7
B: 1,2,3,7,9
A_prime: 2,2,4,5,6
B_prime: 1,3,9

'''

def get_prime_sorted(A, B):
    if not A:
        return [], B

    if not B:
        return A, []

    idx_A, idx_B = 0, 0
    n_A, n_B = len(A), len(B)
    A_prime, B_prime = [], []

    while idx_A < n_A and idx_B < n_B:
        if A[idx_A] > B[idx_B]:
            while idx_B < n_B and A[idx_A] > B[idx_B]:
                B_prime.append(B[idx_B])
                idx_B += 1
        if A[idx_A] < B[idx_B]:
            while idx_A < n_A and A[idx_A] < B[idx_B]:
                A_prime.append(A[idx_A])
                idx_A += 1
        if A[idx_A] == B[idx_B]:
            idx_A += 1
            idx_B += 1

    while idx_A < n_A: 
        A_prime.append(A[idx_A])
        idx_A += 1

    while idx_B < n_B: 
        B_prime.append(B[idx_B])
        idx_B += 1

    return A_prime, B_prime

A = [4, 2, 6, 5, 2, 7, 2]
B = [3, 9, 2, 7, 1]

print(get_prime(A, B))
print(get_prime_sorted(sorted(A), sorted(B)))