import sys
import os
import re

class Preprocessor:
    def __init__(self, lines):
        self.lines = lines

    def eliminate_blank_lines(self):
        """Eliminate blank lines from the lines list."""
        self.lines = [line for line in self.lines if line.strip()]

    def eliminate_comments(self):
        """Eliminate double slash (//) comments and slash-star (/* ... */) comments."""
        for i in range(len(self.lines)):
            # Remove double slash comments
            self.lines[i] = re.sub(r'//.*', '', self.lines[i])
            # Remove multi-line comments
            self.lines[i] = re.sub(r'/\*.*?\*/', '', self.lines[i], flags=re.DOTALL)

    def eliminate_unnecessary_spaces(self):
        """Eliminate unnecessary tabs and spaces."""
        self.lines = [re.sub(r'\s+', ' ', line).strip() for line in self.lines]

    def eliminate_imports_and_annotations(self):
        """Eliminate import statements and annotations."""
        self.lines = [line for line in self.lines if not line.strip().startswith(('import', '@'))]

    def write_to_file(self, output_file_name):
        """Write the processed lines to the specified output file."""
        with open(output_file_name, 'w') as f:
            for line in self.lines:
                f.write(line + '\n')

def main(file_name):
    if not os.path.isfile(file_name):
        print(f"Error: The file '{file_name}' does not exist.")
        return

    with open(file_name, 'r') as f:
        lines = f.readlines()

    preprocessor = Preprocessor(lines)
    preprocessor.eliminate_blank_lines()
    preprocessor.eliminate_comments()
    preprocessor.eliminate_unnecessary_spaces()
    preprocessor.eliminate_imports_and_annotations()

    output_file_name = "out1.txt"
    preprocessor.write_to_file(output_file_name)

    print(f"Processed output written to '{output_file_name}':")
    with open(output_file_name, 'r') as f:
        print(f.read())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
    else:
        main(sys.argv[1])
