class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        
        Given a string s that consists of only uppercase English letters,
        you can perform at most k operations on that string.

        In one operation, you can choose any character of the string and
        change it to any other uppercase English character.

        Find the length of the longest sub-string containing all repeating
        letters you can get after performing the above operations.
        """
        # Maximum number of repeated characters.
        max_repeats = 0

        # Use two pointers `start` and `end` to track a sliding/caterpillar window.
        start = 0

        # Track how many times you see a character in the current window.
        char_freq = {}

	# Length of longest valid substring in the current window.
        max_length = 0

        # Expand the window to the right until the end of the string.
        for end in range(len(s)):
            current_char = s[end]

            # Update `char_freq` by incrementing `current_char` count.
            char_freq[current_char] = char_freq.get(current_char, 0) + 1

            # If `current_char` now has the most repeating characters,
            # update `max_repeats`.
            max_repeats = max(max_repeats, char_freq[current_char])

            current_length = end - start + 1

            # If the number of replacements in order to maximize repeats
            # is less than or equal to `k` operations, update `max_length`.
            if current_length - max_repeats <= k:
                max_length = max(max_length, current_length)

            # Otherwise, slide the window by moving the `start` pointer
            # to the right and update `char_freq` to reflect the new window.
            else:
                char_freq[s[start]] -= 1
                start += 1

        return max_length
