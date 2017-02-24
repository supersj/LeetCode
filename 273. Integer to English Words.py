# Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
#
# For example,
# 123 -> "One Hundred Twenty Three"
# 12345 -> "Twelve Thousand Three Hundred Forty Five"
# 1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# Hint:
#
# Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.
# Group the number by thousands (3 digits). You can write a helper function that takes a number less than 1000 and convert just that chunk to words.
# There are many edge cases. What are some good test cases? Does your code work with input such as 0? Or 1000010? (middle chunk is zero and should not be printed out)
# Subscribe to see which companies asked this question.
class Solution(object):
    def __init__(self):
        self.LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.THOUSANDS = ["", "Thousand", "Million", "Billion"]
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def helper(num):
            if num == 0:
                return ""
            elif num < 20:
                return self.LESS_THAN_20[num] + " "
            elif num < 100:
                return self.TENS[num // 10] + " " + helper(num % 10)
            else:
                return self.LESS_THAN_20[num // 100] + " Hundred" + helper(num % 100)

        if num == 0:
            return "Zero"
        i = 0
        words = ""
        while num > 0:
            if num % 1000  != 0:
                words = helper(num % 1000) + self.THOUSANDS[i] + " " + words
            num //= 1000
            i+=1
        return words.strip()
