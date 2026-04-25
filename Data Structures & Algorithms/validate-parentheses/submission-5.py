class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mp = defaultdict()
        mp[']'] = '['
        mp['}'] = '{'
        mp[')'] = '('

        for char in s:
            if st and st[-1] == mp.get(char):
                st.pop()
            else:
                st.append(char)
        
        return len(st) == 0