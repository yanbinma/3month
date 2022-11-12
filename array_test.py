from util import print_pointers, Pointer
'''
https://www.techinterviewhandbook.org/algorithms/array/
'''

def longestSubString(s, debug=False):
    '''
        https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
        method: sliding window
            use two pointers i, j;
            move j to the right until it meets a repeating character 
                * how to detect repeating: use a hashmap with all existing characters, and their last position(index)
                * when a char is repeated, move i to the next character after the last index of the repeated charater, so that:
                    ** the hashmap doesn't contain any repeated characters, and 
                    ** all character before i are deleted from the hashmap
                    ** update the last position of the new character
            for each substring, measure and store the longest one found up to that point
    '''
    if len(s)<2:
        return s 
    # the start (i) and end (j) of the sliding window
    i = j = 0
    # to remember the last position of each character
    exists = dict()
    exists[s[i]] = 0
    # to remember the longest substring
    maxlen = 1
    # use tuple to remember the longest substr index(s)
    maxsub = (i, j)

    while True:
        if debug: 
            print_pointers(s, Pointer('i', i), Pointer('j', j))
        j += 1
        if j == len(s):
            break 
        if s[j] in exists: 
            for k in range(i, exists[s[j]]):
                del exists[s[k]]
            i = exists[s[j]] + 1            
        exists[s[j]] = j
        if j-i+1 > maxlen:
            maxlen = j-i+1
            maxsub = (i, j)

    return s[maxsub[0]:maxsub[1]+1]

def test_longestSubString():
    #longestSubString("abcdabaabcdefaaabcdefaa", True)
    test_case1 = ["aaaaaaa", "a", "abababa", "abababcda", "abcdabaabcdefaaabcdefaa"]
    for case in test_case1:
        print(f"longestSubString({case}) is {longestSubString(case)}")

test_longestSubString()


