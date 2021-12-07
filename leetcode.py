# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_good(self, path_max, node: TreeNode) -> int:        
        #figure out if current node is good
        #current path maximum from root to current
        # Left, Node, Right
        # Left is_good? => number
        # Right is_good? => number,
        # add those numbers together + my is_good
        # max(x, y) => returns the larger of the two numbers 
        new_path_max = max(path_max, node.val)
        count = 0
        if node.left:
            # option 1:
            # this value is less than path_max, path_max again
            # this values is greater than path_max, pass this value
            count += self.is_good(new_path_max, node.left)
        if node.right:
            count += self.is_good(new_path_max, node.right)
        if node.val >= path_max:
            count += 1
        return count
       
    #.     3 => 4
    #  1 -> 1  4 => 2
    # 3 -> 1  1 => 0  5 => 1
        
    def goodNodes(self, root: TreeNode) -> int:
        #figure out if current is good, then call recursive fxn on left and right
             
        return self.is_good(root.val, root)
    
    
       import collections
       from collections import counter         
def subdomainVisits(self, cpdomains):
    ans = collections.Counter()
    for domain in cpdomains:
        count, domain = domain.split()
        count = int(count)
        frags = domain.split('.')
        for i in range(len(frags)):
            ans[".".join(frags[i:])] += count

    return ["{} {}".format(ct, dom) for dom, ct in ans.items()]
def count_visits(cpdomains):



#pick a center and expand around that center on either side:
def longest_palindrome(letters):
    #if the string is empty, return 0
    if len(letters)==0:
        return 0
    max_len=1
    start=0
    #iterate through my input string
    for i in range(len(letters)):
        #if my current index -max_len is >= 1 (meaning we're not too close to the beginning), 
        # and the characters on either side are the same
        if i-maxLen >=1 and letters[i-maxLen-1:i+1]==letters[i-maxLen-1:i+1][::-1]:
            #then reset the start as current index-(max_len)-1, 
            start=i-max_len-1
            #and add 2 to the max_len cuz we expand out either side
            max_len+=2
            continue
        #if we're too close to the beginning:
        if i-maxLen >=0 and letters[i-maxLen:i+1]==letters[i-maxLen:i+1][::-1]:
            start=i-maxLen
            maxLen+=1
    return len(letters[start:start+maxLen])

print(longest_palindrome("ddrrracecarrr"))


def long_str(letters):
    starting_index = 0
    maximum_length = 0
    checked_chars = {}
    for i in range(len(letters)):
        if letters[i] in checked_chars:
            starting_index = checked_chars[letters[i]] +1
        maximum_length =  i-starting_index +1
        checked_chars[letters[i]] = i
    return maximum_length
# print(long_str("abcdefgabc"))