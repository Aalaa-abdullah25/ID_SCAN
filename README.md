# ID Scanner Application

The **ID Scanner Application** is a user-friendly tool built with **Streamlit** that leverages **Optical Character Recognition (OCR)** technology to extract and display text from uploaded ID images. It is designed to simplify the process of extracting key information from IDs, such as organization names and employee details.

---

## 🚀 Features

- **Image Upload**: Supports multiple image formats, including `.jpg`, `.png`, `.jpeg`, and `.webp`.
- **OCR Processing**: Uses Tesseract OCR to extract text from uploaded images.
- **Organized Output**: Displays extracted text in a structured format:
  - Organization Name
  - Employee Name
  - Additional details from the ID
- **Interactive UI**: Built with Streamlit for a clean and responsive user interface.

---

## 🛠️ Requirements

- **Python**: Version 3.7 or higher
- **Libraries**:
  - `numpy`
  - `streamlit`
  - `pytesseract`
  - `opencv-python`
  - `Pillow`
- **Tesseract OCR**:
  - Installable from [Tesseract GitHub Wiki](https://github.com/UB-Mannheim/tesseract/wiki).

---

## 📦 Installation

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd ID_SCAN
   ```

2. **Install Dependencies**:
   Install the required Python libraries using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Install Tesseract OCR**:
   - Download and install Tesseract OCR from [Tesseract GitHub Wiki](https://github.com/UB-Mannheim/tesseract/wiki).
   - Update the `pytesseract.pytesseract.tesseract_cmd` path in the code to match your Tesseract installation directory.

---

## ▶️ Usage

1. **Run the Application**:
   Launch the Streamlit app by running the following command:

   ```bash
   streamlit run ID_SCAN.py
   ```

2. **Upload an Image**:
   Use the file uploader in the web interface to upload an image of an ID.

3. **View Extracted Text**:
   The extracted text will be displayed in a structured format on the page.

---

## 📂 File Structure

```
ID_SCAN/
├── ID_SCAN.ipynb       # Jupyter Notebook for development
├── ID_SCAN.py          # Main Python script for the Streamlit app
├── requirements.txt    # List of required Python libraries
└── README.md           # Project documentation
```

---

## 📝 Notes

- Ensure that **Tesseract OCR** is installed and properly configured on your system.
- The application assumes a specific format for the ID text. Adjustments may be required for different ID layouts.
- For best results, use high-quality images with clear text.

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---

## 🙌 Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for its powerful OCR capabilities.
- [Streamlit](https://streamlit.io/) for providing an intuitive framework for building interactive web applications.

---

## 💡 Future Enhancements

- Add support for additional languages in OCR.
- Improve text parsing for better accuracy with various ID formats.
- Implement a database to store extracted information for future reference.

---

Feel free to contribute to this project by submitting issues or pull requests. Happy coding! 🚀
