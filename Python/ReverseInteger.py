class Solution:
    def reverse(self, x: int) -> int:
        number = list(map(str, str(x)))
        number.reverse()
        if number[len(number)-1] == "-":
            number.pop()
            number.insert(0,"-")
        new = "".join(number)
        reverse = int(new)
        if reverse > 2**31 or reverse < -2**31:
            reverse = 0
        return reverse
