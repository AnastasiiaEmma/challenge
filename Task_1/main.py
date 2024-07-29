import sys
from Task_1.file_reader import FileReader

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_file> <line_index>")
        sys.exit(1)

    input_file = sys.argv[1]
    line_index = int(sys.argv[2])

    try:
        file_reader = FileReader(input_file)
        line = file_reader.get_line_at_index(line_index)
        print(line)
    except ValueError as e:
        print(e)
