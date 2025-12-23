def mergeSortedArrays(nums1, nums2):
    i = j = 0  # Initialize pointers for both arrays
    result = []  # List to store merged result
    while i < len(nums1) and j < len(nums2):  # Loop while both arrays have elements
        if nums1[i] < nums2[j]:  # If current element in nums1 is smaller
            result.append(nums1[i])  # Add it to result
            i += 1  # Move pointer in nums1
        else:  # Otherwise, current element in nums2 is smaller or equal
            result.append(nums2[j])  # Add it to result
            j += 1  # Move pointer in nums2
    result.extend(nums1[i:])  # Add remaining elements from nums1
    result.extend(nums2[j:])  # Add remaining elements from nums2
    return result  # Return the merged sorted array