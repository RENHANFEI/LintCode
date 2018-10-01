class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        if len(words) == 0:
            return ""
        
        if len(words) == 1:
            return ''.join(sorted(words[0]))
            
        pre_w = words[0]
        bigger_dict = dict({})
        char_indegree = dict({})
        chs = set({})
        chs_ingraph = set({})
        
        for w in words:
            for ww in set(w):
                if ww not in chs:
                    chs.add(ww)
                    
        
        for w in words[1:]:
            # no meaningful info in this case
            if w == pre_w or (w[:len(pre_w)] == pre_w \
                    if len(w) >= len(pre_w) else pre_w[:len(w)] == w):
                continue
            
            for i, ww in enumerate(w):
                if pre_w[i] != ww:
                    chs_ingraph.add(pre_w[i])
                    chs_ingraph.add(ww)
                    if pre_w[i] in bigger_dict:
                        bigger_dict[pre_w[i]].append(ww)  # ww is bigger than pre_w[i]
                    else:
                        bigger_dict[pre_w[i]] = [ww]
                        
                    if ww not in bigger_dict:
                        bigger_dict[ww] = []
                    
                    if pre_w[i] not in char_indegree:
                        char_indegree[pre_w[i]] = 0
                        
                    char_indegree[ww] = 1 if ww not in char_indegree else char_indegree[ww] + 1
                    break
                    
            pre_w = w
            
        
        # get the topograph in bigger_dict
        zero_indegree = []
        for ch, indegree in char_indegree.items():
            if indegree == 0:
                chs.remove(ch)
                zero_indegree.append(ch)
        
        
        res = ""
        cnt = 0
        while len(zero_indegree) != 0:
            zero_indegree.sort()
            out = zero_indegree.pop(0)
            res += out
            cnt += 1
            
            for bigger_than_out in bigger_dict[out]:
                char_indegree[bigger_than_out] -= 1
                if char_indegree[bigger_than_out] == 0:
                    chs.remove(bigger_than_out)
                    zero_indegree.append(bigger_than_out)
        
        if cnt != len(chs_ingraph):
            return ""
        
        
        reminders = sorted(list(chs))
        i = 0
        flag = 0
        for k, ch in enumerate(res):
            if i >= len(reminders):
                break
            while i < len(reminders) and ord(reminders[i]) < ord(ch):
                res = res[:k + flag] + reminders[i] + res[k + flag:]
                flag += 1
                i += 1
        
        res += ''.join(reminders[i:])
                    
        return res