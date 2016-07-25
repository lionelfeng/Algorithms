class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
        	key = self.get_key(s)
        	if dic.get(key):
        		dic.get(key).append(s)
        	else:
        		dic[key] = [s]
        return list(dic.values())

    def get_key(self, s):
    	key = [0] * 26
    	for c in s:
            key[ord(c) - ord('a')] += 1
        return tuple(key)


if __name__ == "__main__":
	print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])