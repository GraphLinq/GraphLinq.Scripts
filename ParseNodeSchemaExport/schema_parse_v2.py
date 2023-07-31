import json
import os

def create_individual_json_files(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

            for idx, item in enumerate(data, start=1):
                node_type = item.get("NodeType", f"item_{idx}")
                file_name = f"{node_type}.json"

                with open(file_name, 'w') as output_file:
                    json.dump(item, output_file, indent=2)

                print(f"Created JSON file for item {idx} (NodeType: {node_type}): {file_name}")

            print(f"\nTotal items processed: {len(data)}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{file_path}'.")

if __name__ == "__main__":
    file_path = "node_schema.json"
    create_individual_json_files(file_path)
