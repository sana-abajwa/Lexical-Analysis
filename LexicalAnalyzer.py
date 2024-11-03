import sys
import os
import re

class LexicalAnalyzer:
    def __init__(self, file_name):
        self.file_name = file_name
        self.keywords = {
            "if", "else", "while", "for", "do", "int", "float", "double",
            "char", "void", "boolean", "true", "false", "return", "class",
            "public", "private", "protected", "static", "final", "try",
            "catch", "throw", "interface"
        }
        self.operators = {
            "+", "-", "*", "/", "%", "=", "+=", "-=", "*=", "/=", "==",
            "!=", "<", ">", "<=", ">=", "++", "--", "&&"
        }
        self.punctuators = {
            "{", "}", "[", "]", "(", ")", ",", ";", ":"
        }
        self.literals_regex = r'(\d+(\.\d+)?|\".*?\"|\'.*?\')'  # integer, float, string, char literals
        self.comments_regex = r'//.*?$|/\*.*?\*/'  # single-line and multi-line comments
        self.import_regex = r'import\s+[\w\.]+;\s*'  # import statements

    def analyze(self):
        """Performs lexical analysis on the input file."""
        with open(self.file_name, 'r') as f:
            content = f.read()

        # Remove comments
        content = re.sub(self.comments_regex, '', content, flags=re.DOTALL)
        # Find import statements
        imports = re.findall(self.import_regex, content)
        content = re.sub(self.import_regex, '', content)  # Remove imports from the content

        # Tokenize the remaining content
        tokens = re.findall(r'\w+|[^\w\s]', content)  # Matches words or single punctuators

        lexemes = {
            "keywords": [],
            "identifiers": [],
            "operators": [],
            "punctuators": [],
            "literals": [],
            "imports": imports
        }

        for token in tokens:
            if token in self.keywords:
                lexemes["keywords"].append(token)
            elif token in self.operators:
                lexemes["operators"].append(token)
            elif token in self.punctuators:
                lexemes["punctuators"].append(token)
            elif re.match(self.literals_regex, token):
                lexemes["literals"].append(token)
            elif re.match(r'^[a-zA-Z_]\w*$', token):  # identifiers start with a letter or underscore
                lexemes["identifiers"].append(token)

        return lexemes

    def display_lexemes(self, lexemes):
        """Displays the categorized lexemes in the specified format."""
        # Create a combined list of lexemes to print in the required format
        for category in ["keywords", "identifiers", "operators", "punctuators", "literals", "imports"]:
            for lexeme in lexemes[category]:
                print(f"Lexeme: {lexeme}")

def main(file_name):
    if not os.path.isfile(file_name):
        print(f"Error: The file '{file_name}' does not exist.")
        return

    analyzer = LexicalAnalyzer(file_name)
    lexemes = analyzer.analyze()
    analyzer.display_lexemes(lexemes)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python lexical_analyzer.py <filename>")
    else:
        main(sys.argv[1])
