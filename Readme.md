# Resume Screener

This project is a **Resume Screener** built using **Flask** and **EasyOCR**. It automates the process of extracting and analyzing text from resumes to streamline candidate screening.

## Features

- Extracts text from resumes (PDF, images, etc.) using EasyOCR.
- Web interface built with Flask for uploading and processing resumes.
- Highlights key information such as name, contact details, skills, and experience.
- Supports multiple languages for OCR.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/resume-screener.git
    cd resume-screener
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Download EasyOCR language models as needed.

## Usage

1. Start the Flask server:
    ```bash
    python app.py
    ```

2. Open your browser and navigate to `http://127.0.0.1:5000`.

3. Upload resumes and view extracted information.

## Dependencies

- Flask
- EasyOCR
- PyTorch
- Other dependencies listed in `requirements.txt`

## Folder Structure

```
resume_screener/
├── app.py               # Main Flask application
├── templates/           # HTML templates
├── static/              # Static files (CSS, JS, etc.)
├── uploads/             # Uploaded resumes
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [EasyOCR](https://github.com/JaidedAI/EasyOCR) for OCR functionality.
- Flask for the web framework.
