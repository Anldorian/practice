def process_string(s: str) -> tuple:
    vowels = "aeiouAEIOU"
    vowel_chars = sorted([char for char in s if char in vowels], reverse=True)
    consonant_chars = sorted([char for char in s if char.isalpha() and char not in vowels], reverse=True)

    has_enough_consonants = len(consonant_chars) >= 4

    return ("".join(vowel_chars), has_enough_consonants, "".join(consonant_chars))

input_string = input("Введіть рядок: ")
result = process_string(input_string)
print(result)
