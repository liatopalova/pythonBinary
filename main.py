
def binary_search(nums, target) -> int:
    min_index = 0
    max_index = len(nums) - 1
    count_try = 0
    while min_index <= max_index:
        count_try += 1
        middle_index = (min_index + max_index) // 2
        if nums[middle_index] == target:
            print(f"Number of tries: {count_try}")
            return middle_index
        else:
            if target < nums[middle_index]:
                max_index = middle_index - 1
            else:
                min_index = middle_index + 1
    return -1


nums_list = list(range(1, 100))
print(nums_list)
try:
    number = int(input("Enter number from 1 to 100: "))
    if 1 > number > 100:
        print("Error number!")
    else:
        result = binary_search(nums_list, number)
        if result != -1:
            print(f"{number} found on index {result}")
        else:
            print("Number not found!")
except ValueError:
    print("Enter only numbers please!")
except Exception as e:
    print(f"Error: {e}")




