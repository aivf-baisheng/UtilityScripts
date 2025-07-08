import subprocess
import os

global cwd

def git_commands():
    """
    Execute a series of git commands to fetch, checkout the main branch, and pull the latest changes.
    """
    try:
        subprocess.run(["git", "fetch"], check=True)
        subprocess.run(["git", "checkout", "dev_main"], check=True)
        subprocess.run(["git", "pull"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing git commands: {e}")

def update_repo(repo_name):
    """
    Update the specified repository by fetching, checking out the main branch, and pulling the latest changes.
    
    Args:
        repo_name (str): Name of the repository to update
    """
    repo_dir = repo_name  # Adjust path if needed

    # Change to the repo directory
    os.chdir(repo_dir)

    # Run git commands
    git_commands()

    os.chdir(cwd)  # Change back to the original directory

def run_npm_build(repo_name):
    """
    Update the specified repository by fetching, checking out the main branch, and pulling the latest changes.
    
    Args:
        repo_name (str): Name of the repository to update
    """
    repo_dir = repo_name  # Adjust path if needed

    # Change to the repo directory
    os.chdir(repo_dir)

    # Run npm build command
    subprocess.run(["npm", "install"], check=True)
    subprocess.run(["npm", "run", "build"], check=True)

    os.chdir(cwd)  # Change back to the original directory

def update_moonshot_data():
    repo_dir = "moonshot-data"  # Adjust path if needed

    update_repo(repo_dir)

def update_moonshot_ui():
    repo_dir = "moonshot-ui"  # Adjust path if needed

    update_repo(repo_dir)

def update_moonshot():
    git_commands()

if __name__ == "__main__":
    # PLEASE PUT THIS SCRIPT IN THE MOONSHOT ROOT DIRECTORY
    # Example: /home/user/code/moonshot/UATHelper.py
    cwd = os.getcwd()
    update_moonshot_data()
    update_moonshot_ui()
    update_moonshot()
    print("Repositories updated successfully.")