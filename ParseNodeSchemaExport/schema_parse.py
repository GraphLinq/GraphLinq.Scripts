import json

def open_and_print_json_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            item_count = len(data)

            print(f"Total items in the JSON file: {item_count}\n")

            for idx, item in enumerate(data, start=1):
                print(f"Item {idx}:")
                print(json.dumps(item, indent=2))
                print("-" * 30)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{file_path}'.")

if __name__ == "__main__":
    file_path = "node_schema.json"  # Replace this with the path to your JSON file.
    open_and_print_json_file(file_path)
