class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Instantiating two variables to hold left and right
        left, right = 0, len(matrix) - 1
        # Instantiating middle variable to mid
        mid = (right + left)//2
        # Iterater until left is less than or equal to right
        while left <= right:
            # If we have found the list that might hold our value then break
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                break
            # Check if the target is greater than the middle starting value
            elif target < matrix[mid][0]:
                # Reset the right pointer to mid minus one
                right = mid - 1
            # Check if the target is less than the middle starting value
            elif target > matrix[mid][0]:
                # Set the left pointer to one past the middle
                left = mid + 1
            # Set the new middle value to the new left and right divided by two
            mid = (right + left) // 2
        # Now that we have found the list that our number might reside in we need to check the list
        nl, nr = 0, len(matrix[mid]) - 1
        # Instantiate new middle as nm to hold the new middle value
        nm = (nl + nr) // 2
        # Repeate the basic process but this time just a standarnd binary search
        while nl <= nr:
            # If the target equals our value return true
            if target == matrix[mid][nm]:
                return True
            # Reset the new left pointer if the target is greater than
            elif target > matrix[mid][nm]:
                nl = nm + 1
            # Reset the new right pointer if the target is less than
            elif target < matrix[mid][nm]:
                nr = nm - 1
            # Update the new middle now that the right or left pointer has been changed
            nm = (nr + nl) // 2
        # Return False if we have not found the number we were looking for
        return False
