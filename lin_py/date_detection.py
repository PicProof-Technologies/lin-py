import re
from typing import List, Tuple, Optional, Dict, Union
import datetime
import logging
xcvb
class DateDetector:
    def __init__(self, additional_patterns: Optional[List[Tuple[str, str]]] = None):
        # Setup logger
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)
        
        # Default date patterns
        self.date_patterns: List[Tuple[re.Pattern, str]] = [
            (re.compile(r'\b(\d{2}[-/\.]\d{2}[-/\.]\d{4})\b'), '%d-%m-%Y'),  # DD-MM-YYYY and variations
            (re.compile(r'\b(\d{2}[-/\. ]\d{2}[-/\. ]\d{4})\b'), '%d %m %Y'),  # DD MM YYYY
            (re.compile(r'\b(\d{8})\b'), '%d%m%Y'),  # DDMYYYY
            (re.compile(r'\b(\d{1,2})\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+(\d{4})\b', re.IGNORECASE), '%d %b %Y'),  # DD Month YYYY
            (re.compile(r'\b(\d{1,2})\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})\b', re.IGNORECASE), '%d %B %Y')  # DD Month YYYY full
        ]

        # Add additional user-defined patterns
        if additional_patterns:
            for pattern, format in additional_patterns:
                self.add_date_pattern(pattern, format)  

    def extract_dates(self, text: str) -> List[Dict[str, Union[str, bool]]]:
        found_dates = []
        for pattern, date_format in self.date_patterns:
            for match in pattern.finditer(text):
                date_str = match.group()
                is_valid = self.validate_date(date_str, date_format)
                found_dates.append({'date': date_str, 'pattern': pattern.pattern, 'is_valid': is_valid})
        return found_dates

    @staticmethod
    def validate_date(date_str: str, date_format: str) -> bool:
        try:
            datetime.datetime.strptime(date_str, date_format)
            return True
        except ValueError:
            return False

    def add_date_pattern(self, pattern: str, date_format: str):
        compiled_pattern = re.compile(pattern)  
        self.date_patterns.append((compiled_pattern, date_format))
        self.logger.info(f"Added new date pattern: {pattern} with format {date_format}")
