
# Random Line Reader

This project provides a Python script to efficiently read a specific line from a very large text file by creating and using an index file of byte offsets.

## Requirements

- Python 3.x

## Installation

1. **Clone the repository or download the scripts**:
   ```git clone ```
   ```cd ```

2.  **Ensure you have Python 3 installed**: Verify your Python version:
```python3 --version```
    

## Usage

1.  **Prepare your input file**: Place your large text file in the same directory as the scripts. For example, `crime_and_punishment.txt`.
    
2.  **Run the script**:
```python3 main.py <input_file> <line_index>```
    
    -   `<input_file>`: Path to the input text file.
    -   `<line_index>`: The zero-based index of the line to retrieve.
    
    Example:
```python3 main.py crime_and_punishment.txt 4```
```python3 main.py crime_and_punishment.txt 589```
```python3 main.py crime_and_punishment.txt 22000```
    

## Files

-   `file_reader.py`: Contains the `FileReader` class which handles indexing and retrieving lines from the input file.
-   `main.py`: The main script to be run from the command line. It uses the `FileReader` class to retrieve and print the specified line.
-   `README.md`: This file, providing an overview and instructions for the project.