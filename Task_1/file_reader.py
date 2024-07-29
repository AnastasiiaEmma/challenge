import os

class FileReader:
    """
    A class to read a specific line from a large text file efficiently
    by creating and using an index file of byte offsets.
    """
    def __init__(self, input_file):
        """
        Initializes the FileReader with the input file path and prepares the index file path.

        :param input_file: Path to the input text file.
        """
        self.input_file = input_file
        self.index_file = input_file + '.idx'
        self.offsets = []

    def create_index_file(self):
        """
        Creates an index file by recording the byte offset of each line's start.
        """
        with open(self.input_file, 'r') as infile, open(self.index_file, 'w') as idxfile:
            offset = 0
            for line in infile:
                idxfile.write(f"{offset}\n")
                offset += len(line)

    def read_index_file(self):
        """
        Reads the index file and stores the byte offsets in a list.
        """
        with open(self.index_file, 'r') as idxfile:
            self.offsets = [int(line.strip()) for line in idxfile]

    def ensure_index_file_exists(self):
        """
        Ensures the index file exists by creating it if necessary,
        and then reads the offsets from the index file.
        """
        if not os.path.exists(self.index_file):
            print(f"Writing index to {self.index_file}... ", end="")
            self.create_index_file()
            print("done.")
        self.read_index_file()

    def get_line_at_index(self, index):
        """
        Retrieves the line at the specified index using the byte offsets.

        :param index: The zero-based index of the line to retrieve.
        :return: The line at the specified index.
        :raises ValueError: If the index is out of range.
        """
        print("Ensuring index file exists.")
        self.ensure_index_file_exists()
        
        print(f"Total lines available: {len(self.offsets)}")
        if index >= len(self.offsets):
            raise ValueError(f"Index {index} out of range. File has {len(self.offsets)} lines.")
        
        byte_offset = self.offsets[index]
        print(f"Byte offset for line {index}: {byte_offset}")
        
        with open(self.input_file, 'r') as infile:
            infile.seek(byte_offset)
            line = infile.readline().strip()
            print(f"Retrieved line: {line}")
            return line