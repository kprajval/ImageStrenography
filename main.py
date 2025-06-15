from Encoder import BinaryEncoder
from Decoder import BinaryDecoder
from ImageToBinaryCode import TextToBinary

InputMessage = input("Enter the message: ")
InputImage = input("Enter the image path: ")

text_obj = TextToBinary(InputMessage)
message_binary = text_obj.TextToBinary()

encoder = BinaryEncoder(InputImage)
encoder.encode(message_binary)
encoded_image_path = "encoded_image.png"
encoder.save_encoded_image(encoded_image_path)
print(f"Message encoded and saved as {encoded_image_path}")

message_length = len(message_binary)
decoder = BinaryDecoder(encoded_image_path)
decoded_message = decoder.decode(message_length)
print(f"Decoded message from image: {decoded_message}")