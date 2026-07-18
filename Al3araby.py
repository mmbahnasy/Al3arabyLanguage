#!/usr/bin/python3

from Al3arabyKeywords import Al3arabyKeywords

variableMap = {}

def main():
    with open("first.3araby", "r", encoding="utf-8") as file:
        for line in file:
            # print(f"line: {line}")
            line = line.replace('\xa0', ' ')
            tokens = line.split(" ")
            print(tokens)
            if tokens:
                try:
                    index = tokens.index(Al3arabyKeywords["declare"])
                    print(f"Tokens: {tokens}")
                    print(f"Token {Al3arabyKeywords['declare']} was found.")
                    if tokens[index+2] == "=":
                        variableMap[tokens[index+1]] = tokens[index+3]
                        print(f"Variable '{tokens[index+1]}' defined with value '{tokens[index+3]}'.")

                except ValueError:
                    continue



if __name__ == "__main__":
    main()
