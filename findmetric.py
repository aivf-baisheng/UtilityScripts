import json
import os
from pathlib import Path

def find_files_with_exact_string(folder_path, target_string="exactstrmatch", field_name="metrics"):
    """
    Find all JSON files in a folder that contain an exact string match in a specified field.
    
    Args:
        folder_path (str): Path to the folder containing JSON files
        target_string (str): The exact string to search for
        field_name (str): The field name to search in
    
    Returns:
        list: List of file paths that contain the exact string match
    """
    matching_files = []
    folder = Path(folder_path)
    
    # Check if folder exists
    if not folder.exists():
        print(f"Error: Folder '{folder_path}' does not exist.")
        return matching_files
    
    # Get all JSON files in the folder
    json_files = list(folder.glob("*.json"))
    
    if not json_files:
        print(f"No JSON files found in '{folder_path}'")
        return matching_files
    
    print(f"Checking {len(json_files)} JSON files...")
    
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Check if the field exists and contains the exact string
            if field_name in data:
                field_value = data[field_name]

                def apply_string_conversion(list, value):
                    list.append(str(value.name))
                
                # Handle different data types for the field
                if isinstance(field_value, str):
                    # For string fields, check for exact match
                    if field_value == target_string:
                        apply_string_conversion(matching_files, json_file)
                elif isinstance(field_value, list):
                    # For list fields, check if exact string is in the list
                    if target_string in field_value:
                        apply_string_conversion(matching_files, json_file)
                elif isinstance(field_value, dict):
                    # For dict fields, check if exact string is in values
                    if target_string in field_value.values():
                        apply_string_conversion(matching_files, json_file)

        except json.JSONDecodeError:
            print(f"Warning: Could not parse JSON file '{json_file}'")
        except Exception as e:
            print(f"Warning: Error reading file '{json_file}': {e}")
    
    return matching_files

def main():
    # Set the folder path (current directory by default)
    folder_path = "/home/user/code/moonshot/moonshot-data/recipes"
    
    # Find matching files
    matching_files = find_files_with_exact_string(folder_path)
    
    # Print results
    if matching_files:
        print(f"\nFound {len(matching_files)} file(s) with exact string 'exactstrmatch' in 'metrics' field:")
        for file_path in matching_files:
            print(f"  {file_path}")
    else:
        print("\nNo files found with the exact string match.")

if __name__ == "__main__":
    main()