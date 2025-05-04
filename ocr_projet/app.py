import os
import google.generativeai as genai
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

# Config Gemini API
os.environ['GEMINI_AI_API_KEY'] = 'AIzaSyBTj-hu5meWc9K23vbHXV3PZDiMwAM6_EE'
API_KEY = os.environ['GEMINI_AI_API_KEY']
genai.configure(api_key=API_KEY)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def prep_pdf(image_path):
    sample_file = genai.upload_file(path=image_path, display_name="Uploaded PDF")
    print(f"Uploaded: {sample_file.display_name} -> {sample_file.uri}")
    return sample_file


def extract_latex_from_pdf(file, prompt):
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    response = model.generate_content([file, prompt])
    return response.text


@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_latex = None

    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            filename = secure_filename(uploaded_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(filepath)

            sample_file = prep_pdf(filepath)

            prompt = (
                """Tu dois convertir ce document PDF en un fichier LaTeX complet, structuré et compilable.

Voici les consignes précises :

1. Génère le texte du document en **français** comme il est écrit (ne pas traduire s'il est déjà en français).
2. Toutes les **formules et expressions mathématiques** doivent être converties correctement en **LaTeX**, avec les bons environnements (`equation`, `align`, etc.).
3. Utilise des balises comme `\section`, `\subsection`, etc. pour structurer le document.
4. Fournis un **document LaTeX complet**, avec le `\documentclass`, l'import des packages nécessaires (ex. `amsmath`, `amssymb`, `geometry`, `babel`, etc.).
5. Le fichier doit pouvoir être compilé sans erreur (par exemple sur Overleaf).
6. N'ajoute aucun commentaire ou explication en dehors du contenu du document original.
7. mettre chaque question a ligne c'est a dire de l'exercice a ligne c'est a dire quand c'est une question il faut laisser une ligne puis passer la suivante

Retourne uniquement le **code source LaTeX** complet, sans aucune explication."""


            )

            extracted_latex = extract_latex_from_pdf(sample_file, prompt)

    return render_template('index.html', extracted_latex=extracted_latex)


if __name__ == '__main__':
    app.run(debug=True)
