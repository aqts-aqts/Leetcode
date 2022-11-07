# Integer to English Words
class Solution:
    def numberToWords(self, num):
        if num == 0: return 'Zero'
        onesWords = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        tensWords = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        tenRanks = {11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        postfix = ['', 'Thousand', 'Million', 'Billion']
        def threeDigitToWord(n):
            if n == 0: return ''
            word = ''
            hundreds = n // 100
            if hundreds > 0: word += onesWords[hundreds - 1] + ' ' + 'Hundred'
            n -= hundreds * 100
            if n in tenRanks: 
                word += ' ' + tenRanks[n]
                return word
            tens = n // 10
            if tens > 0: word += ' ' + tensWords[tens - 1]
            n -= tens * 10
            if n > 0: word += ' ' + onesWords[n - 1]
            return word
        group = ''
        total = []
        for i in range(len(str(num)) - 1, -1, -1):
            group = str(num)[i] + group
            if len(group) == 3: 
                total.append(int(group))
                group = ''
        if len(group) > 0: total.append(int(group))
        word = ''
        for i in range(len(total)):
            if total[i] == 0: continue
            word = (threeDigitToWord(total[i]) + ' ' + postfix[i] + ' ' + word).strip()
        return word