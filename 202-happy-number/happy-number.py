class Solution:
    def isHappy(self, n: int) -> bool:
        history = {}
        current_number = n

        while current_number not in history:
        # Calculate sum of squares using math
            temp = current_number
            new_sum = 0
        
            while temp > 0:
                digit = temp % 10       # Gets the last digit (modulo)
                new_sum += digit ** 2   # Squares it and adds to the sum
                temp = temp // 10       # Removes the last digit
            
        # Store in dictionary
            history[current_number] = new_sum
        
        # Move to the next number
            current_number = new_sum
        
    # Check if 1 is in the history
        return 1 in history