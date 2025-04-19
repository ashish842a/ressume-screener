import os
import json
import easyocr
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from pdf2image import convert_from_path
from fuzzywuzzy import fuzz
import numpy as np

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

reader = easyocr.Reader(['en'], gpu=False)

# Load job configuration from JSON
def load_job_config():
    with open('job_config.json', 'r') as f:
        return json.load(f)

# Extract text from image (ensure it's the correct type)
def extract_text_from_file(file_path):
    print("extraction is in progess....")
    text = ''
    if file_path.lower().endswith('.pdf'):
        images = convert_from_path(file_path)  # Convert PDF to images
        for img in images:
            # Ensure `easyocr` gets a valid image (numpy array)
            result = reader.readtext(np.array(img), detail=0)
            text += ' '.join(result) + ' '
    else:
        # If it's an image, pass the file path or numpy array
        result = reader.readtext(file_path, detail=0)
        text = ' '.join(result)
    return text


def extract_skills(text, required_skills):
    print("fetching skills...")
    words = set(word.lower() for word in text.split())
    matched = []
    for skill in required_skills:
        for word in words:
            if fuzz.ratio(skill.lower(), word) > 80:
                matched.append(skill)
                break
    return list(set(matched))

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    job_config = load_job_config()
    required_skills = job_config["required_skills"]
    job_title = job_config["job_title"]

    if request.method == 'POST':
        file = request.files['resume']
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            text = extract_text_from_file(filepath)
            resume_skills = extract_skills(text, required_skills)

            match_count = len(resume_skills)
            total_required = len(required_skills)
            score = round((match_count / total_required) * 100, 2)
            is_fit = score >= 70

            result = {
                'resume_skills': resume_skills,
                'score': score,
                'is_fit': is_fit
            }

    return render_template('index.html', result=result, job_skills=required_skills, job_title=job_title)

if __name__ == '__main__':
    app.run(debug=True)
