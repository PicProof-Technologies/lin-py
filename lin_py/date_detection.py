import re
from typing import List, Pattern

class DateDetector:

    date_patterns: List[Pattern] = [
        r'\b(\d{2}[-/\.]\d{2}[-/\.]\d{4})\b',  # Matches dates like 04/03/1980, 04-03-1980, 04.03.1980
        r'\b(\d{2}[-/\. ]\d{2}[-/\. ]\d{4})\b',  # Matches dates like 04 03 1980
        r'\b(\d{8})\b',  # Matches concatenated dates like 04031980
        r'Date of Birth: ?(\d{2}[./-]\d{2}[./-]\d{4})',  # Matches 'Date of Birth: 04.03.1980'
        r'Date of Birth: ?(\d{8})',  # Matches 'Date of Birth:01001970'
        r'Date of Birth: ?(\d{2}[-/\. ]\d{2}[-/\. ]\d{4})',  # Matches 'Date of Birth: 04 03 1980'
        r'\b(\d{1,2})\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+(\d{4})\b',  # Matches '14 Jan 2024'
        r'\b(\d{1,2})\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})\b'  # Matches '14 February 2024'
    ]

    @staticmethod
    def extract_date(text: str) -> str:
       
        for pattern in DateDetector.date_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group()
        return "Date not found"

    @staticmethod
    def validate_date(date_str: str) -> bool:
        
        try:
            datetime.datetime.strptime(date_str, '%d-%m-%Y')
            return True
        except ValueError:
            return False
