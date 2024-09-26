import pandas as pd
import numpy as np
import locale

def process_flex_file(file_path):
    # Set locale to German to handle commas as decimal separators
    locale.setlocale(locale.LC_NUMERIC, 'de_DE.UTF-8')

    # Read the FLEX file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Process the lines and create a DataFrame
    data = []
    for line in lines:
        parts = line.strip().split('|')
        if len(parts) > 1:
            name = parts[0]
            values = [process_value(val) for val in parts[1:]]
            data.append([name] + values)

    df = pd.DataFrame(data)

    # Remove rows where all elements are NaN
    df = df.dropna(how='all')

    # Remove columns where all elements are NaN
    df = df.dropna(axis=1, how='all')

    # Reset index after removing rows
    df = df.reset_index(drop=True)

    # Ensure all numeric columns have one decimal place
    for col in df.columns[1:]:
        df[col] = pd.to_numeric(df[col], errors='coerce').round(1)

    return df

def process_value(x):
    x = str(x).strip()  # Remove leading and trailing whitespace
    x = x.replace('\xa0', '')  # Remove non-printable spaces
    x = x.replace('Teiler', '').strip()  # Remove "Teiler" and whitespace
    try:
        return locale.atof(x)  # Convert string to float considering locale
    except ValueError:
        print(f"Could not convert value '{x}'")
        return np.nan
