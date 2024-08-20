import pytesseract
from pytesseract import Output
from typing import Optional
import numpy as np 
class TextExtractor:
    

    tesseract_cmd: str = '/usr/local/bin/tesseract'

    @staticmethod
    def configure_tesseract(cmd_path: str):
        
        TextExtractor.tesseract_cmd = cmd_path

    @staticmethod
    def extract_text(image: np.ndarray, language: str = 'eng') -> str:
       
        pytesseract.pytesseract.tesseract_cmd = TextExtractor.tesseract_cmd
        return pytesseract.image_to_string(image, lang=language, output_type=Output.STRING)
