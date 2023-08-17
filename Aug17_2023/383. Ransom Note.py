class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result = True
        for i in ransomNote:
            if i in magazine and ransomNote.count(i) <= magazine.count(i):
                result = True
            else:
                return False
        return result