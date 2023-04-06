class Solution:
    def __init__(self):
        # Define a dictionary that maps Roman numerals to integer values
        self.roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def int_to_roman(self, s):
        # Define a dictionary that maps integer values to Roman numerals
        roman_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
                      500: 'D', 900: 'CM', 1000: 'M'}
        result = ""
        # Loop through the dictionary in descending order of value
        for value, numeral in sorted(roman_dict.items(), reverse=True):
            # Subtract the largest possible value from the input number until it reaches zero
            while s >= value:
                result += numeral
                s -= value
        return result

    def get_input(self):
        # Prompt the user for input and store it in the instance variable 'input_str'
        self.input_str = input("Input: s = ")

    def to_int(self):
        result = 0
        prev_value = 0
        # Loop through each character in the input string
        for c in self.input_str:
            curr_value = self.roman_dict[c]
            # If the current value is greater than the previous value, subtract twice the previous value
            if curr_value > prev_value:
                result += curr_value - 2 * prev_value
            else:
                result += curr_value
            prev_value = curr_value
        return result

    def display(self):
        # Convert the input string to an integer using the 'to_int' method
        integer_value = self.to_int()
        # Convert the integer to a Roman numeral using the 'int_to_roman' method
        roman_value = self.int_to_roman(integer_value)
        roman_values = {}
        # Loop through each character in the Roman numeral and add its value to the 'roman_values' dictionary
        for numeral in roman_value:
            if numeral not in roman_values:
                roman_values[numeral] = self.roman_dict[numeral]
            else:
                roman_values[numeral] += self.roman_dict[numeral]
        # Print the output and explanation
        print("Output:", integer_value)
        print("Explanation: ", end="")
        for numeral, value in roman_values.items():
            print(numeral, "=", value, end=", ")
        # Remove the last comma and space characters and print a period
        print("\b\b.")

# Create an instance of the Solution class and call its methods
result = Solution()
result.get_input()
result.display()
