def f(strings, s):
    upper = set([chr(c) for c in range(ord('A'), ord('Z') + 1)])
    string_lists = []
    for string in strings:
        lead = 0
        string_list = []
        for i, ch in enumerate(string[1:]):
            if ch in upper:
                string_list.append(string[lead:i + 1])
                lead = i + 1
        string_list.append(string[lead:])
        string_lists.append(string_list)

    string_list = []
    lead = 0
    for i, ch in enumerate(s[1:]):
        if ch in upper:
            string_list.append(s[lead:i + 1])
            lead = i + 1
    string_list.append(s[lead:])

    ans = []

    for name in string_lists:
        valid = True
        for i, substring in enumerate(string_list):
            if i >= len(name) or not is_valid(substring, name[i]):
                valid = False
                break
        if valid:
            ans.append(''.join(name))

    return ans

def is_valid(substring, s):
    if len(substring) > len(s):
        return False
    for i, ch in enumerate(substring):
        if ch != s[i]:
            return False
    return True

strings = [ "GraphView",
"DataGraphView",
"DataController",
"GraphViewController",
"DataScienceView"]

print(f(strings, "GraphController"))