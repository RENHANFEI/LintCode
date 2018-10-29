def decode(ciphertext):
    encrypt = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    decrypt = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    dictionary = dict(zip(encrypt, decrypt))

    if not ciphertext:
        return

    start = 0
    plaintext = []
    while start < len(ciphertext):
        end = start
        while end < len(ciphertext) and ciphertext[end] != ' ': 
            end += 1
        plaintext.append(dictionary[ciphertext[start:end]])
        start = end + 1

    return ''.join(plaintext)

x = ".- -... -.-."
print(decode(x))


# def wordBreak(s):
#     """
#     :type s: str
#     :type wordDict: Set[str]
#     :rtype: List[str]
#     """
#     encrypt = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
#     decrypt = [chr(i) for i in range(ord('a'), ord('z') + 1)]
#     wordDict = dict(zip(encrypt, decrypt))

#     return helper(s, wordDict, {})
    
# def helper(s, wordDict, memo):
#     if s in memo: return memo[s]
#     if not s: return []
    
#     res = []
#     for word, val in wordDict.items():
#         if not s.startswith(word):
#             continue
#         if len(word) == len(s):
#             res.append(val)
#         else:
#             resultOfTheRest = helper(s[len(word):], wordDict, memo)
#             for item in resultOfTheRest:
#                 item = val + item
#                 res.append(item)
#     memo[s] = res
#     return res

# print(wordBreak(x.replace(' ', '')))

def wordBreak2(s):
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: List[str]
    """
    encrypt = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    decrypt = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    wordDict = dict(zip(encrypt, decrypt))

    return helper2(s, wordDict)
    
def helper2(s, wordDict):
    if not s: return []
    
    res = []
    for word, val in wordDict.items():
        if not s.startswith(word):
            continue
        if len(word) == len(s):
            res.append(val)
        else:
            resultOfTheRest = helper2(s[len(word):], wordDict)
            for item in resultOfTheRest:
                item = val + item
                res.append(item)
                
    return res

print(wordBreak2(x.replace(' ', '')))
