import pandas as pd
import io

def analyze_data(df):
    # Flatten the dataframe to a series of (name, value) pairs
    flat_data = [(row[0], val) for _, row in df.iterrows() for val in row[1:] if pd.notnull(val)]
    
    # Sort the flattened data by value (ascending order)
    sorted_data = sorted(flat_data, key=lambda x: x[1])
    
    # Get the 12 smallest unique values with their names
    result = []
    seen = set()
    for name, value in sorted_data:
        if value not in seen:
            result.append((name, value))
            seen.add(value)
            if len(result) == 12:
                break
    
    # Nummeriere die Ergebnisse von 1 bis 12
    numbered_result = [(i+1, name, value) for i, (name, value) in enumerate(result)]
    
    return numbered_result

def create_csv(data):
    df = pd.DataFrame(data, columns=['Rang', 'Name', 'Wert'])
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    return csv_buffer.getvalue()