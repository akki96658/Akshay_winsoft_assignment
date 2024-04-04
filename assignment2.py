def longest_substring_without_repeating(s: str) -> int:
    max_length = 0
    char_index_map = {}
    start = 0

    for end in range(len(s)):
        if s[end] in char_index_map:
            start = max(start, char_index_map[s[end]] + 1)

        char_index_map[s[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length

# Example usage:
s1 = "abcabcbb"
print(longest_substring_without_repeating(s1))  # Output: 3

s2 = "bbbbb"
print(longest_substring_without_repeating(s2))  # Output: 1

s3 = "pwwkew"
print(longest_substring_without_repeating(s3))  # Output: 3