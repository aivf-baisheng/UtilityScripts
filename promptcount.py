import json

MOONSHOT_ROOT_DIR = "/home/user/code/moonshot"

def read_json_file(file_path):
    """
    Read a JSON file and return its contents
    
    Args:
        file_path (str): Path to the JSON file
    
    Returns:
        dict/list: The parsed JSON data
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{file_path}'. {e}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def parse_dataset(file_path):

    json_data = read_json_file(file_path)

    if json_data is not None:
        prompt_count = len(json_data["examples"])
        print("    Dataset '"+json_data["name"]+"' Prompt Count: "+ str(prompt_count))
    else:
        print(file_path + " is not a valid dataset file.")
        raise ValueError("Invalid JSON data or file not found.")
    return prompt_count

def create_dataset_path(file_name):
    """
    Create a dataset path based on the file name
    
    Args:
        file_name (str): Name of the file
    
    Returns:
        str: Path to the dataset
    """
    return f"{MOONSHOT_ROOT_DIR}/moonshot-data/datasets/{file_name}.json"

def parse_recipe(file_path):

    json_data = read_json_file(file_path)

    if json_data is not None:
        print("\n  Recipe Name: " + json_data["name"])
        prompt_count = 0
        percent_prompt_count = 0
        for datasets in json_data["datasets"]:
            dataset_prompt = parse_dataset(create_dataset_path(datasets))
            prompt_count += dataset_prompt
            percent_prompt_count += max(1, dataset_prompt//100)

    else:
        print(file_path + " is not a valid recipe file.")
        raise ValueError("Invalid JSON data or file not found.")
    
    print("  Total Prompt Count in Recipe: " + str(prompt_count))
    print("  Total percent Prompt Count in Recipe: " + str(percent_prompt_count))


    return prompt_count, percent_prompt_count

def create_recipe_path(file_name):
    """
    Create a recipe path based on the file name
    
    Args:
        file_name (str): Name of the file
    
    Returns:
        str: Path to the recipe
    """
    return f"{MOONSHOT_ROOT_DIR}/moonshot-data/recipes/{file_name}.json"

def parse_cookbook(file_path):

    json_data = read_json_file(file_path)

    if json_data is not None:
        print("Cookbook Name: " + json_data["name"])
        prompt_count = 0
        percent_prompt_count = 0
        for recipes in json_data["recipes"]:
            prompts, ppcount = parse_recipe(create_recipe_path(recipes))
            prompt_count += prompts
            # theres no 0 prompt minimum 1 for recipes
            percent_prompt_count += ppcount
    else:
        # If the file is not valid, raise an error
        print(file_path + " is not a valid cookbook file.")
        raise ValueError("Invalid JSON data or file not found.")

    print("\nTotal Prompt Count in Cookbook: " + str(prompt_count))
    print("1 Percent Prompt Count in Cookbook: " + str(percent_prompt_count))

def print_line():
    """
    Print a separator line
    """
    print("=" * 50)

# Main execution
if __name__ == "__main__":

    print_line()
    parse_cookbook(MOONSHOT_ROOT_DIR +"/moonshot-data/cookbooks/hallucination.json")
    print_line()
    parse_cookbook(MOONSHOT_ROOT_DIR +"/moonshot-data/cookbooks/data-disclosure.json")
    print_line()
    parse_cookbook(MOONSHOT_ROOT_DIR +"/moonshot-data/cookbooks/undesirable-content.json")
    print_line()
    parse_cookbook(MOONSHOT_ROOT_DIR +"/moonshot-data/cookbooks/adversarial-attacks.json")
    print_line()

    # parse_recipe("/home/user/code/moonshot/moonshot-data/recipes/mmlu.json")

    # # Replace 'your_file.json' with the path to your JSON file
    # 
    # json_file_path = "/home/user/code/moonshot/moonshot-data/datasets/cyberseceval-promptinjection2-en.json"
    # 
    # # Read the JSON file
    # json_data = read_json_file(json_file_path)
    # 
    # if json_data is not None:
    #     print("Prompt Count:")
    #     print("=" * 50)       
    #     print(len(json_data["examples"]))
  
        