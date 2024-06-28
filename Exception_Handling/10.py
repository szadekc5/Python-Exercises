def test_list_operation(nums):
    try:
        
        r1 = nums.length  
        
        print("Length of the list:", r1)
    except AttributeError:
        
        print("Error: The list does not have a 'length' attribute.")


nums = [1, 2, 3, 4, 5]

test_list_operation(nums)
