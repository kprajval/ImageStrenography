from PIL import Image
import numpy as np


class ImageToBinaryCode:
    def __init__(self, path):
        self.imagePath = path
        self.image = Image.open(self.imagePath).convert("RGB")
        self.pixels = np.array(self.image)
        self.bits = None

    def ToFlattenBinaryCode(self):
        self.bits = np.unpackbits(self.pixels.astype(np.uint8))
        return self.bits

    def BitsToImage(self):
        if self.bits is None:
            raise ValueError("You must call ToFlattenBinaryCode() before PathToImage().")
        restored_pixels = np.packbits(self.bits)
        restored_pixels = restored_pixels.reshape(self.pixels.shape)
        restored_image = Image.fromarray(restored_pixels, 'RGB')
        return restored_image

class TextToBinary:
    def __init__(self, message=""):
        self.message = message
        self.binary_code = ""

    def TextToBinary(self):
        self.binary_code = ''.join(format(ord(char), '08b') for char in self.message)
        return self.binary_code

    def BinaryToText(self, binary_code):
        chars = [chr(int(binary_code[i:i+8], 2)) for i in range(0, len(binary_code), 8)]
        return ''.join(chars)
