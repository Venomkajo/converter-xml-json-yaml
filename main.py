import os
import xml
import json
import yaml

ALLOWED_EXTENSIONS = ['.xml', '.json', '.yaml', '.yml']

def main():
    input_file = 'test.xml'
    output_file = 'test.json'
    converter(input_file, output_file)

def converter(input_file, output_file):
    try:
        input_ext = os.path.splitext(input_file)[1]
        output_ext = os.path.splitext(output_file)[1]
    except IndexError:
        raise ValueError("Invalid file name; must include name and extension")

    if input_ext not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Unsupported input file extension: {input_ext}")
    if output_ext not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Unsupported output file extension: {output_ext}")

main()