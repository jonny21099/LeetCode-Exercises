class Solution:
    def isPalindrome(self, x: int) -> bool:
        palindrome_list = list(map(str, str(x)))
        original_list = list(map(str, str(x)))
        counter = 0
        palindrome_list.reverse()
        for each in range(len(palindrome_list)):
            if palindrome_list[each] == original_list[each]:
                counter += 1
                if counter == len(palindrome_list):
                    return True
            else:
                return False
