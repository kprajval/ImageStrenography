# Image Steganography — Text in Image LSB

## Project Overview

This project allows you to hide a secret text message inside an image using **Least Significant Bit (LSB) steganography**.  
The message is converted to binary and embedded within the image's pixel data.  
It also includes functionality to decode and extract the hidden message from the image.

## Modules

- **ImageToBinaryCode.py**: Converts image to bits and back.
- **TextToBinary.py**: Converts text to binary and back.
- **Encoder.py**: Encodes a message's binary bits into the image's bits.
- **Decoder.py**: Extracts message bits from image and converts them to text.
- **main.py**: User interface to run the full encode/decode process.

## Output
Enter the message: hello world!
Enter the image path: uwp4803195.png
Message encoded and saved as encoded_image.png
Decoded message from image: hello world!

Process finished with exit code 0

