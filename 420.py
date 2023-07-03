# Strong Password Checker
class Solution:
    def strongPasswordChecker(self, password):
        missing = 3 - any(char.islower() for char in password) - any(char.isupper() for char in password) - any(char.isdigit() for char in password)
        replace = 0
        replaceOnes = 0
        replaceTwos = 0
        i = 2
        while i < len(password):
            if password[i] == password[i - 1] == password[i - 2]:
                cur = 2 
                while i < len(password) and password[i - 1] == password[i]:
                    cur += 1
                    i += 1
                replace += cur // 3
                replaceOnes += int(cur % 3 == 0)
                replaceTwos += int(cur % 3 == 1)
            else:
                i += 1

        result = max(0, len(password) - 20)
        if len(password) > 20:
            voids = len(password) - 20
            replace -= min(voids, replaceOnes)
            voids = max(0, voids - replaceOnes)
            replace -= min(voids, replaceTwos * 2) // 2
            voids = max(0, voids - replaceTwos * 2)
            replace -= voids // 3
        result += max(6 - len(password), missing, replace)
        return result