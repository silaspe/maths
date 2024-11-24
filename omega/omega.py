from enum import Enum, auto
import re
from typing import List
import sys

class TokenType(Enum):
	Number = auto()
	Identifier = auto()
	Equals = auto()
	OpenParen = auto()
	CloseParen = auto()
	BinaryOperator = auto()

class Token:
    def __init__(self, value: str, type: TokenType):
        self.value = value
        self.type = type

    def __repr__(self):
        return f"Token(value={self.value!r}, type={self.type!r})"


def tokenize(codeString: str) -> List[Token]:
    tokens = []
    index = 0

    # Define multi-character operators
    multi_char_operators = {"==", ">=", "<=", "!="}

    while index < len(codeString):
        char = codeString[index]

        # Skip whitespace
        if char.isspace():
            index += 1
            continue

        # Match numbers
        if char.isdigit():
            num_value = char
            index += 1
            while index < len(codeString) and codeString[index].isdigit():
                num_value += codeString[index]
                index += 1
            tokens.append(Token(value=num_value, type=TokenType.Number))
            continue

        # Match identifiers (letters and potentially followed by alphanumeric characters)
        if char.isalpha():
            identifier = char
            index += 1
            while index < len(codeString) and (codeString[index].isalnum() or codeString[index] == "_"):
                identifier += codeString[index]
                index += 1
            tokens.append(Token(value=identifier, type=TokenType.Identifier))
            continue

        # Match multi-character operators
        if index + 1 < len(codeString):
            two_char_sequence = codeString[index:index+2]
            if two_char_sequence in multi_char_operators:
                tokens.append(Token(value=two_char_sequence, type=TokenType.BinaryOperator))
                index += 2
                continue

        # Match single-character operators
        if char in "=()+-*/,":  # Fixed comma from BinaryOperator typo
            token_type = {
                "=": TokenType.Equals,
                "(": TokenType.OpenParen,
                ")": TokenType.CloseParen,
                "+": TokenType.BinaryOperator,
                "-": TokenType.BinaryOperator,
                "*": TokenType.BinaryOperator,
                "/": TokenType.BinaryOperator,
                ",": TokenType.BinaryOperator,
            }.get(char, None)
            if token_type is not None:
                tokens.append(Token(value=char, type=token_type))
                index += 1
                continue

        # If no match, raise an error (unexpected character)
        print(f"Unexpected character: {char} at {index}")
        index += 1  # Ensure the index is incremented to avoid getting stuck

    return tokens


def main():
    if len(sys.argv) < 2:
        print("Usage: python tokenizer.py <file.om>")
        return

    filename = sys.argv[1]

    # Read the .om file
    with open(filename, "r") as file:
        source_code = file.read()

    # Tokenize the file
    tokens = tokenize(source_code)

    # Print the tokens
    for token in tokens:
        print(token)

if __name__ == "__main__":
    main()