# # Import your classes from their respective files
# from Preprocessor import Preprocessor
# from Processor import Processor
# from LexicalAnalyzer import LexicalAnalyzer

# # Function to read the Java file content
# def read_file(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             return file.read()
#     except FileNotFoundError:
#         print("File not found. Please check the file path.")
#     except IOError:
#         print("An error occurred while reading the file.")
   

# if __name__ == "__main__":
#     # Replace this with the actual path to your Java file
#     file_path = "C:\\Users\\sanaa\\Desktop\\MS DataScience\\Python\\Assignment_1\\File1.java"
    
#     # Step 1: Read the content of the Java file
#     content = read_file(file_path)
    
#     if content:
#         # Step 2: Create instances of the classes
#         preprocessor = Preprocessor(file_path)
#         processor = Processor(file_path)
#         LexicalAnalyzers = LexicalAnalyzer(file_path)
        
#         # Step 3: Process the content through your pipeline
#         #preprocessed_content = preprocessor.preprocess(content)
#         processed_content = processor.process(preprocessed_content)
#         LexicalAnalyzer.analyze(processed_content)
        
#         # Print a completion message
#         print("Lexical Analysis Completed.")



# Import your classes from their respective files
from Preprocessor import Preprocessor
from Processor import Processor
from LexicalAnalyzer import LexicalAnalyzer

# Function to read the Java file content
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except IOError:
        print("An error occurred while reading the file.")
    return None  # Return None if an error occurs

if __name__ == "__main__":
    # Replace this with the actual path to your Java file
    file_path = "C:\\Users\\sanaa\\Desktop\\MS DataScience\\Python\\Assignment_1\\File1.java"
    
    # Step 1: Read the content of the Java file
    content = read_file(file_path)
    
    if content:
        # Step 2: Create instances of the classes
        preprocessor = Preprocessor(file_path)  # Initialize with the file path
        processor = Processor(file_path)  # Initialize without arguments, if not needed
        lexical_analyzer = LexicalAnalyzer(file_path)  # Initialize without arguments, if not needed
        
        # Step 3: Process the content through your pipeline
        preprocessed_content = preprocessor.preprocess()  # Call the preprocess method
        processed_content = processor.process()  # Process the preprocessed content
        lexical_analyzer.analyze()  # Call analyze on the lexical analyzer instance
        
        # Print a completion message
        print("Lexical Analysis Completed.")
    else:
        print("No content to process.")