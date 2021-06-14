class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        len_of_str = min([(len(i),strs.index(i)) for i in strs])
        for i in range(len_of_str[0]):
            current_letter = strs[len_of_str[1]][i]
            flag = False
            ct = 0
            for j in strs:
                if j[i] == current_letter:
                    ct += 1
                else:
                    flag = True
            if ct == len(strs) and flag == False:
                res += current_letter
            else:
                break
        return res
        
            
