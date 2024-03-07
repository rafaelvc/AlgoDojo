def strStr(haystack: str, needle: str) -> int:
    if len(haystack) < len(needle):
        return -1
    i = 0
    while (len(haystack) - i)+1 > len(needle):
        if haystack[i] == needle[0] and haystack[i:i+len(needle)] == needle:
        # if haystack[i:i+len(needle)] == needle:
            return i
        i += 1
    return -1

haystack, needle  = "zadbutsad", "sad"
print (strStr(haystack, needle))

haystack, needle  = "xad", "sad"
print (strStr(haystack, needle))
