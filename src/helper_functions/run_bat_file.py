import subprocess
import os
# from dotenv import load_dotenv
# # load_dotenv()

def run_bat_file():
    """Runs the run1090 batch file using subprocess to begin ADS-B data collection."""

    bat_file_path = "C:\\Users\\dylan\\OneDrive\\Desktop\\Projects\\src\\Dump1090-main\\run1090.bat"
    folder_path = os.path.dirname(bat_file_path)
    print(f"Starting batch file: {bat_file_path}")

    return subprocess.Popen(
        bat_file_path,
        cwd=folder_path, # Set the working directory to where the .bat file is located
        shell=True,     
        text=True    # Decodes the output from bytes to text
    )
    