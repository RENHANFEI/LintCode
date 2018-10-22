class Solution:
    """
    @param s: a string
    @return: reverse only the vowels of a string
    """
    def reverseVowels(self, s):
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels_positions = []
        vowels_in_string = []
        
        for i, ss in enumerate(s):
            if ss in vowels:
                vowels_positions.append(i)
                vowels_in_string.append(ss)
        
        len_vowels = len(vowels_positions)
        
        if len_vowels <= 1:
            return s
        

        for i, v1 in enumerate(vowels_in_string[0:len_vowels // 2]):
            pos1 = vowels_positions[i]
            pos2 = vowels_positions[len_vowels - i -1 ]
            v2 = vowels_in_string[len_vowels - i - 1]
            
            s = s[:pos1] + v2 + s[pos1 + 1:]
            s = s[:pos2] + v1 + s[pos2 + 1:]

        
        return s