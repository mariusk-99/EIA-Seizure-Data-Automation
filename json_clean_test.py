import json

def clean_and_parse_json(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Correctly handle escape sequences by decoding them
    # This step assumes the file contains JSON with escaped newline and quote characters
    # that should be interpreted literally.
    cleaned_content = bytes(content, "utf-8").decode("unicode_escape")
    
    # Parse the cleaned content as JSON
    try:
        json_data = json.loads(cleaned_content)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None
    
    return json_data

# Example usage
file_path = 'extracted_data/Website_3.json'
parsed_json = clean_and_parse_json(file_path)
if parsed_json is not None:
    print(parsed_json)