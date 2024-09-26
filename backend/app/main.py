from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import tempfile
import io
import json
from services.file_processor import process_ods_file
from services.data_analyzer import analyze_data, create_csv

app = Flask(__name__)
CORS(app)  # Dies erlaubt CORS für alle Routen

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Keine Datei im Request gefunden'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Keine Datei ausgewählt'}), 400
    
    if file and file.filename.endswith('.ods'):
        try:
            # Temporäre Datei erstellen
            with tempfile.NamedTemporaryFile(delete=False, suffix='.ods') as temp_file:
                file.save(temp_file.name)
                
                # ODS-Datei verarbeiten
                df = process_ods_file(temp_file.name)
                
                # Daten analysieren
                result = analyze_data(df)
                
            return jsonify({'result': result})
        except Exception as e:
            return jsonify({'error': f'Fehler bei der Verarbeitung der Datei: {str(e)}'}), 500
    
    return jsonify({'error': 'Ungültiger Dateityp. Bitte laden Sie eine .ods Datei hoch.'}), 400

@app.route('/download', methods=['GET'])
def download_csv():
    data = request.args.get('data')
    if not data:
        return jsonify({'error': 'Keine Daten zum Herunterladen bereitgestellt'}), 400
    
    try:
        result = json.loads(data)
        csv_data = create_csv(result)
        
        return send_file(
            io.BytesIO(csv_data.encode()),
            mimetype='text/csv',
            as_attachment=True,
            download_name='result.csv'
        )
    except json.JSONDecodeError:
        return jsonify({'error': 'Ungültiges JSON-Format für die Daten'}), 400
    except Exception as e:
        return jsonify({'error': f'Fehler beim Erstellen der CSV-Datei: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(port=4000, debug=True)
