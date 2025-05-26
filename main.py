import os, sys
import xml, json, yaml

ALLOWED_EXTENSIONS = ['.xml', '.json', '.yaml', '.yml']

def main():
    if len(sys.argv) < 3:
        print("Usage: main.py <input_file> <output_file>")
        return 1
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    converter(input_file, output_file)

def converter(input_file, output_file):
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")
    if os.path.isfile(output_file):
        raise FileExistsError(f"Output file already exists: {output_file}")

    try:
        input_ext = os.path.splitext(input_file)[1]
        output_ext = os.path.splitext(output_file)[1]
    except IndexError:
        raise ValueError("Invalid file name; must include name and extension")

    if input_ext not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Unsupported input file extension: {input_ext}")
    if output_ext not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Unsupported output file extension: {output_ext}")
    
    if input_ext == '.json':
        with open(input_file, 'r') as input:
            try:
                input_data = json.load(input)
            except Exception as e:
                raise ValueError(f"Error reading JSON file: {e}")
            
    if output_ext == '.json':
        with open(output_file, 'w') as output:
            try:
                json.dump(input_data, output)
            except Exception as e:
                raise ValueError(f"Error writing JSON file: {e}")

main()