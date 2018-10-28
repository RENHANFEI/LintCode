def f(meetings, new_meeting):
    if not meetings:
        return True
    meetings.sort()
    if new_meeting[1] <= meetings[0]:
        return True    # new meeting ends before the first starts
    for meeting in meetings:
        if new_meeting[0] < meeting[1]:
            if new_meeting[1] <= meeting[0]:
                return True
            else:
                return False
    return True


meetings = [[1300, 1500], [930, 1200],[830, 845]]
new = [820, 830]
new2 = [1450, 1500]

print(f(meetings, new))
print(f(meetings, new2))

def f2(intervals):
    if not intervals:
        return

    intervals.sort()
    ans = []

    if intervals[0][0] > 0:
        ans.append([0, intervals[0][0]])

    pre_end = intervals[0][1]

    for interval in intervals[1:]:
        if interval[0] > pre_end:
            ans.append([pre_end, interval[0]])
        pre_end = interval[1]

    return ans


intervals = [[1300, 1500], [930, 1200],[830, 845], [820, 830], [1450, 1500]]
print(f2(intervals))