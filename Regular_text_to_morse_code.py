symbols = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": ".-", "h": "....", "i": "..",
    "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",
}

# Taking data from the user
data = input("Enter text: ")

length = len(data)

# Converting to Morse code 
output = [symbols.get(data[i]) for i in range(length) if data[i] in symbols.keys()]

print(' '.join(output))

#end
