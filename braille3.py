# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 21:37:47 2023

@author: DIPTENDU
"""

braille_mapping = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋',
    'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇',
    'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗',
    's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭',
    'y': '⠽', 'z': '⠵', '  ':' ',
    '0': '⠼⠴', '1': '⠼⠂', '2': '⠼⠆', '3': '⠼⠒', '4': '⠼⠲',
    '5': '⠼⠢', '6': '⠼⠖', '7': '⠼⠶', '8': '⠼⠦', '9': '⠼⠔'
}

def to_braille(text):
    converted_text = ""
    for char in text:
        if char.lower() in braille_mapping:
            converted_text += braille_mapping[char.lower()]
    return converted_text

def from_braille(braille_text):
    reversed_mapping = {v: k for k, v in braille_mapping.items()}
    converted_text = ""
    while braille_text:
        braille_char = braille_text[:2] if braille_text.startswith('⠼') else braille_text[:1]
        if braille_char in reversed_mapping:
            converted_text += reversed_mapping[braille_char]
        braille_text = braille_text[len(braille_char):]
    return converted_text

# Example usage
text = input("Enter text to convert to Braille: ")
braille_text = to_braille(text)
print("Braille representation:", braille_text)

braille_input = input("Enter Braille text to convert back: ")
converted_text = from_braille(braille_input)
print("Braille to Character converted text:", converted_text)
