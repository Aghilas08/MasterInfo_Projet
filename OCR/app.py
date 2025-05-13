import os
import re
# from PIL import Image, ImageEnhance
from io import BytesIO
import google.generativeai as genai
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

# Config Gemini API
API_KEY = 'AIzaSyBXfxG0C2YwZHMv9fcxoDm9Pr6rAt4EIJc'
genai.configure(api_key=API_KEY)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


class TextExtractor:
    def __init__(self, api_key):
        self.api_key = api_key
        genai.configure(api_key=api_key)
    
    def extract_text_from_image(self, image_path):
        """
        Extrait le texte à partir d'une image de document en utilisant Gemini, je veux avoir le rendu en makdown propre 
        """
        try:
            # Uploader le fichier pour Gemini
            sample_file = genai.upload_file(path=image_path, display_name="Document")
            
            # Configurer le modèle avec le nom correct
            # Utiliser le nom de modèle correct selon la documentation Google
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")
            
            # Préparer le prompt
            prompt = """Renvoie tout le texte visible dans l'image en format Markdown.
            Si tu vois un nom et prénom, mets-les en évidence."""
            
            # Générer la réponse
            response = model.generate_content([sample_file, prompt])
            
            # Traiter la réponse
            if response:
                return response.text.strip()
            
            return "Aucun texte extrait"
            
        except Exception as e:
            print(f"Erreur lors de l'extraction du texte: {e}")
            return f"Erreur: {str(e)}"


# Fonctions Flask
def prep_pdf(image_path):
    try:
        sample_file = genai.upload_file(path=image_path, display_name="Uploaded PDF")
        print(f"Uploaded: {sample_file.display_name} -> {sample_file.uri}")
        return sample_file
    except Exception as e:
        print(f"Erreur lors de l'upload du fichier: {e}")
        return None


def extract_latex_from_pdf(file, prompt):
    try:
        # Utilisez le nom correct du modèle
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content([file, prompt])
        return response.text
    except Exception as e:
        print(f"Erreur lors de l'extraction: {e}")
        return f"Erreur: {str(e)}"


@app.route('/ocr', methods=['GET', 'POST'])
def index():
    extracted_latex = None
    extracted_text = None
    error_message = None

    if request.method == 'POST':
        if 'file' not in request.files:
            error_message = "Aucun fichier sélectionné"
            return render_template('index.html', error_message=error_message)
            
        uploaded_file = request.files['file']
        if uploaded_file.filename == '':
            error_message = "Aucun fichier sélectionné"
            return render_template('index.html', error_message=error_message)
            
        try:
            filename = secure_filename(uploaded_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(filepath)

            # Extraction du template LaTeX
            sample_file = prep_pdf(filepath)
            if sample_file:
                prompt = """Tu dois convertir ce document PDF en un fichier LaTeX complet, structuré et compilable.

                        Voici les consignes précises :

                        1. Génère le texte du document en **français** comme il est écrit (ne pas traduire s'il est déjà en français).
                        2. Toutes les **formules et expressions mathématiques** doivent être converties correctement en **LaTeX**, avec les bons environnements (`equation`, `align`, etc.).
                        3. Utilise des balises comme `\section`, `\subsection`, etc. pour structurer le document.
                        4. Fournis un **document LaTeX complet**, avec le `\documentclass`, l'import des packages nécessaires (ex. `amsmath`, `amssymb`, `geometry`, `babel`, etc.).
                        5. Le fichier doit pouvoir être compilé sans erreur (par exemple sur Overleaf).
                        6. N'ajoute aucun commentaire ou explication en dehors du contenu du document original.
                        7. mettre chaque question a ligne c'est a dire de l'exercice a ligne c'est a dire quand c'est une question il faut laisser une ligne puis passer la suivante

                        Retourne uniquement le **code source LaTeX** complet, sans aucune explication.
                        """
                
                extracted_latex = extract_latex_from_pdf(sample_file, prompt)
                
                # Extraction du texte
                extractor = TextExtractor(API_KEY)
                extracted_text = extractor.extract_text_from_image(filepath)
            else:
                error_message = "Erreur lors de l'upload du fichier"
                
        except Exception as e:
            error_message = f"Une erreur est survenue: {str(e)}"

    return render_template('index.html', 
                          extracted_latex=extracted_latex, 
                          extracted_text=extracted_text,
                          error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True ,host="0.0.0.0", port=5002)