class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = {}
        for c in magazine:
            note[c] = 1 + note.get(c,0)

        for c in ransomNote:
            if c not in note or note[c] <= 0:
                return False
            note[c] = note[c] - 1
        
        return True














        # Map = {}
        # for c in magazine:
        #     Map[c] = 1 + Map.get(c, 0)

        # for c in ransomNote:
        #     if (c not in Map or Map[c] <= 0):
        #         return False
        #     Map[c] = Map.get(c) - 1

        # return True