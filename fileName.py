import os
import pandas as pd

def log_file_info(file_path):
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return

    # Check if the file is an Excel or CSV file
    if file_path.endswith('.csv'):
        # Read the CSV file
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        # Read the Excel file
        df = pd.read_excel(file_path)
    else:
        print(f"Unsupported file type: {file_path}")
        return

    # Get the number of lines
    num_lines = len(df)

    # Get the file name
    file_name = os.path.basename(file_path)

    # Log the number of lines and file name to the console
    print(f"File Name: {file_name}")
    print(f"Number of Lines: {num_lines}")

# Example usage
file_path = input("G:\My Drive\Ayam and.or Internal\Clients\Chaikel Travel\Reports\August 26 2024.xlsx")
log_file_info(file_path)