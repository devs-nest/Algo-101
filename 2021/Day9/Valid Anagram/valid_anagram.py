class Solution:
    	def isAnagram(self, s: str, t: str) -> bool:
		ns, nt = len(s), len(t)
		if ns != nt: return False
		if ns == 0 and nt == 0: return True
		elif ns == 0 or nt == 0: return False
		return self.isAnagram(s.replace(s[0], ''), t.replace(s[0], ''))