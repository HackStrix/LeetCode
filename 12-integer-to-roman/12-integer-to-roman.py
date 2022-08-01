def intToRomanHelper(num: int, roman: str) -> str:
        if num == 0:
            return roman
        elif num >= 1000:
            num-=1000
            return intToRomanHelper(num,roman+"M")
        elif num >= 900:
            num-=900
            return intToRomanHelper(num, roman+"CM")
        elif num >= 500:
            num-=500
            return intToRomanHelper(num, roman+"D")
        elif num >= 400:
            num-=400
            return intToRomanHelper(num, roman+"CD")
        elif num >= 100:
            num-=100
            return intToRomanHelper(num, roman+"C")
        elif num >= 90:
            num-=90
            return intToRomanHelper(num, roman+"XC")
        elif num >= 50:
            num-=50
            return intToRomanHelper(num, roman+"L")
        elif num >= 40:
            num-=40
            return intToRomanHelper(num, roman+"XL")
        elif num >= 10:
            num-=10
            return intToRomanHelper(num, roman+"X")
        elif num >= 9:
            num-=9
            return intToRomanHelper(num, roman+"IX")
        elif num >= 5:
            num-=5
            return intToRomanHelper(num, roman+"V")
        elif num >= 4:
            num-=4
            return intToRomanHelper(num, roman+"IV")
        else:
            num-=1
            return intToRomanHelper(num, roman+"I")
class Solution:
    
        
    def intToRoman(self, num: int) -> str:
        return intToRomanHelper(num,"")