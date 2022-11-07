# Strong Password Checker II
class Solution:
    def strongPasswordCheckerII(self, password):
        password = password.replace('"', '')
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digit = '0123456789'
        special = '!@#$%^&*()-+'
        a=0
        u=0
        d=0
        s=0

        if len(password) < 8:
            return False
        for i in range(1, len(password)):
            if password[i - 1] == password[i]:
                return False
            if password[i] in alpha: a+=1
            if password[i] in upper: u+=1
            if password[i] in digit: d +=1
            if password[i] in special: s+=1
        if password[0] in alpha: a+=1
        if password[0] in upper: u+=1
        if password[0] in digit: d +=1
        if password[0] in special: s+=1
        if a>0 and u>0 and d>0 and s>0: return True
        return False