from PIL import Image
import numpy as np
from ImageToBinaryCode import ImageToBinaryCode

class BinaryEncoder:
    def __init__(self, image_path):
        self.image_obj = ImageToBinaryCode(image_path)
        self.image_obj.ToFlattenBinaryCode()
        self.bits = self.image_obj.bits.copy()
        self.original_shape = self.image_obj.pixels.shape

    def encode(self, message_binary):
        if len(message_binary) > len(self.bits):
            raise ValueError("Message too large to encode in image.")

        for i in range(len(message_binary)):
            self.bits[i] = int(message_binary[i])

    def save_encoded_image(self, output_path):
        restored_pixels = np.packbits(self.bits)
        restored_pixels = restored_pixels.reshape(self.original_shape)
        restored_image = Image.fromarray(restored_pixels, 'RGB')
        restored_image.save(output_path)
