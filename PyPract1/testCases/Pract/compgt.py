#8.In Python the comparison operator > when used with string operands compares the string character by character.
# Write a snippet to compare two string operands based on their length; hint: Implement __gt__ method
class LengthComparator:
    def __init__(self, value):
        self.value = value

    def __gt__(self, other):
        if isinstance(other, str):
            return len(self.value) > len(other)
        else:
            raise TypeError("Comparison with unsupported type")

    def __str__(self):
        return self.value


# Test the LengthComparator class
str1 = LengthComparator("apple")
str2 = LengthComparator("banana")
str3 = LengthComparator("cherry")

print(str1 > str2)  # Outputs: False
print(str2 > str1)  # Outputs: True
print(str2 > str3)  # Outputs: False
