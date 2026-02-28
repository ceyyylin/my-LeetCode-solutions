# runtime: 11 ms, beats 58.69%
# writes strings in a zigzag pattern

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # creating a rail fence cipher
        if numRows <= 1:
            return s
        rails = [""] * numRows # creates a list like ["", "", ""]
        row = 0
        direction = 1 # 1 for down, -1 for up
        for char in s:
            rails[row] += char # adds the char to the current spot
            row += direction # move to the next row, didn't write a constant value so it change directions
            if row == 0 or row == numRows - 1:
                direction *= -1 # multiply by -1 to change direction
        return "".join(rails) # combine all chars