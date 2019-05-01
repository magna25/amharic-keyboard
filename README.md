# Amharic-keyboard

### Demo
https://amharic.io

This is a simple python package that lets you type Amharic letters using Latin alphabet. 

It will analyze the given Latin text for consonants + vowels and converts those words in to the equaivalent of Amharic words.

It follws the same pattern used for typing Amharic words when texting.

# Installation:

`pip install amharic-keyboard`

or simply grab keyboard.py and import that.

requires python 3

# usage

```
import amharic_keyboard as ak

print(ak.type("selam nachihu?"))  

#prints:
     ሰላም ናችሁ?

```

# bugs

windows console doesn't support custom fonts so you won't be able to see the converted characters.

