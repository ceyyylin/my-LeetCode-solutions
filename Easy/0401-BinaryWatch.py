# runtime: 0 ms, beats 100.00%
# creates a list of possible times depending on the number of lights turned on
# used bit manipulation and brute force

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        results = [] # create an empty list
        for hour in range(12):
            for minute in range(60):
                # summation of the lights for hours and minutes
                total_lights = self.find_light_num(hour) + self.find_light_num(minute)

                if total_lights == turnedOn:
                    time = f"{hour}:{minute:02d}" # 02d is to make it two digits
                    results.append(time) # add it to the list

        return results

    def find_light_num(self, number):
        return bin(number).count("1") # count the number of 1s to find the amount of lights