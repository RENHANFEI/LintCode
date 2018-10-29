from collections import deque

def poke_moles(holes, hammer_length):
    if hammer_length >= len(holes):
        return sum(holes)

    hit = deque(holes[:hammer_length])
    pre_moles = sum(hit)
    max_moles = pre_moles

    for hole in holes[hammer_length:]:
        moles = pre_moles + hole - hit.popleft()
        pre_moles = moles
        max_moles = max(max_moles, moles)
        hit.append(hole)

    return max_moles

def poke_moles_2(holes, hammer_length):
    if hammer_length * 2 >= len(holes):
        return sum(holes)

    
    hit = deque(holes[:hammer_length])
    pre_moles = sum(hit)
    max_moles = pre_moles
    sub_max_moles = [max_moles]  # max_moles[i]: max hits from 0 to i + hammer_length

    for hole in holes[hammer_length:]:
        moles = pre_moles + hole - hit.popleft()
        pre_moles = moles
        max_moles = max(max_moles, moles)
        hit.append(hole)
        sub_max_moles.append(max_moles)

    print(sub_max_moles)

    hit = deque(holes[-hammer_length:])
    pre_moles = sum(hit)
    max_moles = pre_moles
    sub_max_moles_2 = [max_moles] # max_moles_2[i]: max hits from len + i - hammer_length to len - i

    for hole in holes[:-hammer_length][::-1]:
        moles = pre_moles + hole - hit.pop()
        pre_moles = moles
        max_moles = max(max_moles, moles)
        hit.appendleft(hole)
        sub_max_moles_2.append(max_moles)

    print(sub_max_moles_2)
        
    ans = 0
    for i in range(hammer_length, len(holes) - hammer_length):
        moles = sub_max_moles[i - hammer_length] + sub_max_moles_2[len(holes) - hammer_length - i]
        ans = max(moles, ans)

    return ans



array = [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0]
hammer_length = 5
print(poke_moles(array, hammer_length))
print(poke_moles_2(array, hammer_length))

