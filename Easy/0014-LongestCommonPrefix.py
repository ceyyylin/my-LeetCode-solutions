# runtime: 4 ms, beats 9.21% (find out a faster way)
# compares two strings and finds the longest common prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # get the first word and store it as a reference
        prefix = strs[0]

        # check if the word starts with the reference, if not crop the reference until they match
        for str in strs[1:]:
            while str[:len(prefix)] != prefix:
                prefix = prefix[:-1]

                # if nothing matches return empty
                if not prefix:
                    return ""

        return prefix