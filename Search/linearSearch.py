#Linear Search
def linear_search(arr, target):
    for num in arr:
        if num == target:
            return num  # Return the index of the found target
    return -1  # Return -1 if the target is not found


# Example Usage
data = [10, 20, 30, 40, 50]
target_value = 30

result = linear_search(data, target_value)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")


# Time Complexity -> n is length of list
# Best - O(1) - constant
# Avg - O(n) - linear
# Worst - O(n) - linear

# Space Complexity
# Best, Avg, Worst - O(1)