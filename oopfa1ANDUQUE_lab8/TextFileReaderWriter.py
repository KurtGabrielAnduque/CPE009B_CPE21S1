from FileReaderWriter import FileReaderWriter

class TextFileReaderWriter(FileReaderWriter):
    def read(self, filepath):

        try:
            with open(filepath, 'r') as file:
                data = file.read()
                print("Text File Content:")
                print(data)
                return data
        except FileNotFoundError:
            print(f"Error: The file {filepath} does not exist.")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")

    def write(self, filepath, data):

        try:
            with open(filepath, 'w') as file:
                file.write(data)
                print(f"Data has been written to {filepath}.")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")