import pandas as pd
import numpy as np
import locale

def process_ods_file(file_path):
    # Setze das Locale auf Deutsch, um Kommas als Dezimaltrennzeichen zu behandeln
    locale.setlocale(locale.LC_NUMERIC, 'de_DE.UTF-8')

    # Lese die ODS-Datei
    df = pd.read_excel(file_path, engine='odf')
    
    # Entferne Zeilen, in denen alle Elemente NaN sind
    df = df.dropna(how='all')
    
    # Entferne Spalten, in denen alle Elemente NaN sind
    df = df.dropna(axis=1, how='all')
    
    # Entferne Header-Zeilen (angenommen, die erste Spalte ist immer ein Name)
    while not pd.api.types.is_string_dtype(df.iloc[:, 0]):
        df = df.iloc[1:]
    
    # Setze den Index zurück nach dem Entfernen von Zeilen
    df = df.reset_index(drop=True)
    
    # Verarbeite 'Teiler'-Werte und konvertiere zu float
    for col in df.columns[1:]:
        df[col] = df[col].apply(lambda x: process_value(x) if pd.notnull(x) else np.nan)
    
    # Stelle sicher, dass alle numerischen Spalten eine Dezimalstelle haben
    for col in df.columns[1:]:
        df[col] = df[col].round(1)
    
    return df

def process_value(x):
    if isinstance(x, (int, float)):
        return float(x)
    x = str(x).strip()  # Entferne Leerzeichen am Anfang und Ende
    x = x.replace('\xa0', '')  # Entferne nicht-druckbare Leerzeichen
    x = x.replace('Teiler', '').strip()  # Entferne "Teiler" und Leerzeichen
    try:
        return locale.atof(x)  # Konvertiere String zu float unter Berücksichtigung des Locales
    except ValueError:
        print(f"Konnte den Wert '{x}' nicht konvertieren")
        return np.nan