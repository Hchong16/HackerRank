# Minimum number of distinct elements after removing m items
# Question: https://www.geeksforgeeks.org/minimum-number-of-distinct-elements-after-removing-m-items/

if __name__ == "__main__":
    arr = [2, 4, 1, 5, 3, 5, 1, 3]
    m = 2

    # Create hash table to hold all count of each unique IDs
    countDict = {}

    for num in arr:
        if num in countDict.keys():
            countDict[num] += 1
        else:
            countDict[num] = 1

    # Remove m elements and update hash table
    for num in range(0, m):
        countDict[arr[num]] -= 1

        if countDict[arr[num]] <= 0:
            countDict.pop(arr[num], None)

    # Print unique IDs
    print("Output: {}".format(len(countDict.keys())))
