def printEvenNos(n):
    for i in range(1, n+1): #Loop from 1 to n (inclusive), so use range(1, n+1)
        if i % 2 == 0:        # Check if the current number i is even
            print(i) # Print the even number
