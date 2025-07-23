class Solution:
    def reverseWords(self, s: str) -> str:
    # Convert string to list to allow in-place editing
        chars = list(s)
        n = len(chars)
    
        # Step 1: Clean spaces (in-place)
        def clean_spaces(chars):
            n = len(chars)
            i = 0  # Read pointer
            j = 0  # Write pointer
            while i < n:
                # Skip leading spaces
                while i < n and chars[i] == ' ':
                    i += 1
                # Copy the next word
                while i < n and chars[i] != ' ':
                    chars[j] = chars[i]
                    j += 1
                    i += 1
                # Skip spaces between words
                while i < n and chars[i] == ' ':
                    i += 1
                # Add single space if next word exists
                if i < n:
                    chars[j] = ' '
                    j += 1
            return chars[:j]
        
        chars = clean_spaces(chars)
        n = len(chars)
        # Step 2: Reverse entire string
        chars.reverse()
        
        # Step 3: Reverse each word
        def reverse_word_range(chars, left, right):
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        
        start = 0
        for i in range(n + 1):
            if i == n or chars[i] == ' ':
                reverse_word_range(chars, start, i - 1)
                start = i + 1
        
        return ''.join(chars)

        