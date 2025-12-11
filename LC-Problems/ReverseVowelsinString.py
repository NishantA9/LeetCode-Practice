class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return s
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}  # vowel set for fast checks
        s = list(s)  # convert to list for in-place swaps
        l, r = 0, len(s) - 1  # two pointers from both ends  # noqa: E741
        while l < r:
            if s[l] not in vowel:
                l += 1  # move left pointer until vowel found # noqa: E741
            elif s[r] not in vowel:
                r -= 1  # move right pointer until vowel found
            else:
                s[l], s[r] = s[r], s[l]  # swap the vowels
                l, r = l+1, r-1  # advance both pointers # noqa: E741
        return "".join(s)  # join list back to string