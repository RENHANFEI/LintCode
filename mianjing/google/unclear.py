times = [1,0,1,5,1,0,2]
scales = [[0,1],[5,6],[2,3]]

def f(times, scales):
    for scale in scales:
        for i in range(scale[0], scale[1] + 1):
            times[i] += 1

    return times

print(f(times, scales))