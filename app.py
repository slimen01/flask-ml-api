import torch
from flask import Flask, request, jsonify
from PIL import Image
import os
# Charger le modèle
model = torch.load('best.pt', map_location=torch.device('cpu'), weights_only=False)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur l'API de prédiction !"

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    try:
        # Ouvrir l'image
        image = Image.open(file)
        
        # TODO: ajouter ici le traitement d'image et la prédiction avec le modèle
        # Exemple : transformation en tensor, normalisation, etc.

        # Exemple de réponse temporaire
        return jsonify({'message': 'File processed successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))  # Utilise le port de Render, sinon 5000 localement
    app.run(host='0.0.0.0', port=port)