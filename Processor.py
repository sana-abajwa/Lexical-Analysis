import sys
import os

class Processor:
    def __init__(self, file_name):
        self.file_name = file_name
        self.buffer = []

    def read_file(self):
        """Reads the file character by character and populates the buffer."""
        with open(self.file_name, 'r') as f:
            while True:
                char = f.read(1)  # Read one character at a time
                if not char:  # Break on EOF
                    break
                if char != '\n':  # Ignore newline characters
                    self.buffer.append(char)
        
        # Add sentinel value at the end of the buffer
        self.buffer.append('$')

    def write_to_file(self, output_file_name):
        """Writes the buffer to the specified output file."""
        with open(output_file_name, 'w') as f:
            f.write(''.join(self.buffer))

    def display_output(self, output_file_name):
        """Displays the contents of the output file on the console."""
        with open(output_file_name, 'r') as f:
            print(f.read())

def main(file_name):
    if not os.path.isfile(file_name):
        print(f"Error: The file '{file_name}' does not exist.")
        return

    processor = Processor(file_name)
    processor.read_file()

    output_file_name = "out2.txt"
    processor.write_to_file(output_file_name)

    print(f"Processed output written to '{output_file_name}':")
    processor.display_output(output_file_name)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python processor.py <filename>")
    else:
        main(sys.argv[1])
