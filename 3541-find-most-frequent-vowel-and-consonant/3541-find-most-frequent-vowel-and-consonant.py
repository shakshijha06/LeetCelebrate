class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiou"
        
        vowel_count = {}
        consonant_count = {}

        for ch in s.lower():
            if ch.isalpha():
                if ch in vowels:
                    vowel_count[ch] = vowel_count.get(ch, 0) + 1
                else:
                    consonant_count[ch] = consonant_count.get(ch, 0) + 1

        max_vowel = max(vowel_count.values(), default=0)
        max_consonant = max(consonant_count.values(), default=0)

        return max_vowel + max_consonant