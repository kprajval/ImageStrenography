from PIL import Image
import numpy as np

class BinaryDecoder:
    def __init__(self, image_path):
        self.image = Image.open(image_path).convert("RGB")
        self.pixels = np.array(self.image)
        self.bits = np.unpackbits(self.pixels.astype(np.uint8))

    def decode(self, message_length):
        extracted_bits = self.bits[:message_length]
        binary_str = ''.join(str(bit) for bit in extracted_bits)
        chars = [chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8)]
        return ''.join(chars)
