from typing import List
# Define a class named Solution
class Solution:

    # Define a method named singleNumber that takes a list of integers as input
    # and returns a single integer that appears only once in the list
    def singleNumber(self, nums: List[int]) -> int:
        result = 0  # Initialize a variable named result to 0
        for num in nums:  # Iterate over each number in the input list
            result ^= num  # Perform the XOR operation between result and the current number
            # This effectively cancels out all the duplicate numbers in the list,
            # leaving only the single number that appears once
        return result  # Return the resulting single number

# Create an instance of the Solution class
search = Solution()

# Prompt the user to enter a list of integers separated by spaces
num_list = input("Enter a list of numbers separated by space: ")
# Split the entered string using the split method and convert it into a list of integers
nums = [int(num) for num in num_list.split()]

# Print the input list of integers
print("Input: nums=", nums)

# Call the singleNumber method and store the result
result = search.singleNumber(nums)

# Print the single number
print("Output:", result)
