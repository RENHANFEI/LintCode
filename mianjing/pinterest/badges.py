def f1(records):
    no_exit = set()
    no_enter = set()
    for name, record in records:
        if record == 'enter':
            if name in no_enter:
                no_enter.remove(name)
            else:
                no_exit.add(name)
        else:    # exit
            if name in no_exit:
                no_exit.remove(name)
            else:
                no_enter.add(name)
    return no_exit, no_enter

badge_records = [
["Martha",   "exit"],
["Paul",     "enter"],
["Martha",   "enter"],
["Martha",   "exit"],
["Jennifer", "enter"],
["Paul",     "enter"],
["Curtis",   "enter"],
["Paul",     "exit"],
["Martha",   "enter"],
["Martha",   "exit"],
["Jennifer", "exit"],
["Scott",    "exit"]]

print(f1(badge_records))

# We want to find employees who badged into our secured room unusually often. 
# We have an unordered list of names and access times over a single day. 
# Access times are given as three or four-digit numbers using 24-hour time, such as "800" or "2250".
# Write a function that finds anyone who badged into the room 3 or more times in a 1-hour period, 
# and returns each time that they badged in during that period. 
# (If there are multiple 1-hour periods where this was true, just return the first one.)

from collections import defaultdict, deque

def f2(records):
    records.sort(key=lambda record: record[1])
    name_records = defaultdict(lambda: deque())
    counted = set()
    ans = []

    for name, time in records:
        if name in counted:
            continue
        name_record = name_records[name]
        if len(name_record) >= 3:
            start = name_record[0]
            if time - start <= 100:
                name_record.append(time)
            else:
                ans.append((name, name_record))
                counted.add(name)
        elif len(name_record) == 2:
            start = name_record[0]
            if time - start <= 100:
                name_record.append(time)
            else:
                name_record.pop()
                name_record.append(time)
        else:
            name_record.append(time)

    return ans


badge_records = [
["Paul", 1355],
["Jennifer", 1910],
["John", 830],
["Paul", 1315],
["John", 835],
["Paul", 1405],
["Paul", 1630],
["John", 855],
["John", 915],
["John", 930],
["Jennifer", 1335],
["Jennifer", 730],
["John", 1630],
]

print(f2(badge_records))
