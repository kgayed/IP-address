class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Replace all occurrences of '.' with '[.]' using the replace method
        return address.replace('.', '[.]')

# Create an instance of the Solution class
finder = Solution()

# Prompt the user to enter an IP address
address = input("Input: address = ")

# Call the defangIPaddr method with the input IP address as argument and store the result
result = finder.defangIPaddr(address)

# Print the resulting defanged IP address
print("Output:", result)
