import cv2
import numpy as np

class ImageProcessor:
    def __init__(self, image_path: str):
        self.image_path = image_path
        self.image = None

    def read_image(self) -> np.ndarray:
        self.image = cv2.imread(self.image_path)
        if self.image is None:
            raise FileNotFoundError(f"No image found at {self.image_path}")
        return self.image

    def convert_to_grayscale(self) -> np.ndarray:
        if self.image is None:
            raise ValueError("No image has been loaded. Please load an image first.")
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def apply_threshold(self, threshold_value: int = 150) -> np.ndarray:
        gray_image = self.convert_to_grayscale()
        _, thresh = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)
        return thresh

    def preprocess_image(self) -> np.ndarray:
        self.read_image()
        gray = self.convert_to_grayscale()
        thresh = self.apply_threshold()
        return thresh
