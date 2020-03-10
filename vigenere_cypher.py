from string import ascii_lowercase
from enum import Enum

alphabet = ascii_lowercase

class Mode(Enum):
    ENCODE = 1
    DECODE = 2

def sub_key_generator(key):
	while True:
		for letter in key:
			yield letter

def translate_text(text, key, mode):
	_sub_key_generator = sub_key_generator(key)

	return "".join([translate_letter(char, next(_sub_key_generator), mode) if char.lower() in alphabet else char for char in text])

def translate_letter(letter, subkey, mode):
	plain_text_index = alphabet.index(letter.lower())
	sub_key_index = alphabet.index(subkey.lower()) 
	if mode == Mode.ENCODE:
		cypher_letter_index = (plain_text_index + sub_key_index)%len(alphabet)
	elif mode == Mode.DECODE:
		cypher_letter_index = (plain_text_index - sub_key_index)%len(alphabet)

	return alphabet[cypher_letter_index] if letter.islower() else alphabet[cypher_letter_index].upper()

def encode_text(text,key):
	return translate_text(text, key, Mode.ENCODE)

def decode_text(text,key):
	return translate_text(text, key, Mode.DECODE)

if __name__ == '__main__':

	with open("plain_text.txt", "r") as file:
		print(file.read())
