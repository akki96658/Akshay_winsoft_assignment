def non_repeating_characters(s: str) -> str:
    char_frequency = {}

    # Counting the frequency of each character
    for char in s:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    # Filter out characters with frequency 1
    non_repeating_chars = [char for char, freq in char_frequency.items() if freq == 1]

    return ''.join(non_repeating_chars)

# Example use:
s = "abacddbec"
print(non_repeating_characters(s))  # Output: 'e'