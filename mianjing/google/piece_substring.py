def piece_number(A, B):
    if not is_invalid(A, B):
        raise Exception("Invalid Input!")

    if not A:
        return B

    idx_A = 0
    n_A, n_B = len(A), len(B)
    num = 0

    while idx_A < n_A:
        max_match = 0
        for idx_B in range(n_B):
            if B[idx_B] == A[idx_A]:    # optimize: record every letter's position in B in a dictionary
                match = 1
                while (match + idx_B < n_B and 
                    match + idx_A < n_A and 
                    B[idx_B + match] == A[idx_A + match]):
                    match += 1
                max_match = max(max_match, match)
        num += 1
        idx_A += max_match

    return num

def is_invalid(A,B):
    # TODO: validation
    return True


A = 'zabaz'
B = 'azab'

print(piece_number(A, B))