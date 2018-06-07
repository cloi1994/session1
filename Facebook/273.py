class Solution(object):
    def numberToWords(self, num):
        
        if num == 0:
            return "Zero"
        else:
            res = self.intToWords(num)
            print res
            return res[1:len(res)]
        
        
        
    def intToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        digits = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["Zero", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        
        if num >= 1000000000:
            return self.intToWords(num/1000000000) + " Billion" + self.intToWords(num%1000000000)
        elif num >= 1000000:
            return self.intToWords(num/1000000) + " Million" + self.intToWords(num%1000000)
        elif num >= 1000:
            return self.intToWords(num/1000) + " Thousand" + self.intToWords(num%1000)
        elif num >= 100:
            return self.intToWords(num/100) + " Hundred" + self.intToWords(num%100)        
        elif num >= 20:
            return " " + tens[num / 10] + self.intToWords(num % 10)
        elif num >= 1:
            return " " + digits[num]
        else:
            return ""
        
        
        
