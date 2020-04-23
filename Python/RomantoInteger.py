class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        Conversion = {"I": 1, "V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        romanList = list(s)
        for i, v in enumerate(romanList):
            if i == len(romanList) - 1:
                value = Conversion.get(v)
            elif (v == "I" and romanList[i+1] == "V") or (v == "I" and romanList[i+1] == "X"):
                value = -1
            elif (v == "X" and romanList[i+1] == "L") or (v == "X" and romanList[i+1] == "C"):
                value = -10 
            elif (v == "C" and romanList[i+1] == "D") or (v == "C" and romanList[i+1] == "M"):
                value = -100
            else:
                value = Conversion.get(v)
            sum += value
        return sum
