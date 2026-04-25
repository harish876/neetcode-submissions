class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, curr, n = 0, 0, len(s)
        seen_map, need_map = {}, Counter(t) 
        seen, need = 0, len(set(t))
        result = ""
        min_len = float("inf")
        
        while curr < n:
            seen_map[s[curr]] = seen_map.get(s[curr],0) + 1

            if seen_map[s[curr]] == need_map.get(s[curr],-1):
                seen += 1

            while seen == need:
                tmp = s[left: curr+1]
                if len(tmp) < min_len:
                    result = tmp
                    min_len = len(tmp)
                
                seen_map[s[left]] -= 1
                if seen_map[s[left]] <= 0:
                    del seen_map[s[left]]
                
                if s[left] in need_map and seen_map.get(s[left],-1) < need_map[s[left]]:
                    seen -= 1
                
                left +=1
                
            curr +=1 

        return result