def f(scales, target):
    print(target)
    t_start, t_end = target
    for start, end in scales:
        if start >= t_start:
            if end <= t_end:
                return True
        else:
            if f(scales, (t_start - start, t_end - end)): return True
    return False


scales = [[100, 150], [200, 240], [200, 280], [400, 410]]
targets = [[100, 110], [90, 120], [300, 360], [310, 360], [1, 9999999999], [300, 450]]

# for target in targets:
#     print(f(scales, target))

print(f(scales, [300, 400]))