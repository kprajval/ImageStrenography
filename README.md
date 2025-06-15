<h1>Image Steganography — Text in Image LSB</h1>

    <h2>Project Overview</h2>
    <p>This project allows you to hide a secret text message inside an image using Least Significant Bit (LSB) steganography.
    The message is converted to binary and embedded within the image's pixel data.
    It also includes functionality to decode and extract the hidden message from the image.</p>

    <h2>Modules</h2>
    <ul>
        <li><strong>ImageToBinaryCode.py</strong>: Converts image to bits and back</li>
        <li><strong>TextToBinary.py</strong>: Converts text to binary and back</li>
        <li><strong>Encoder.py</strong>: Encodes a message's binary bits into the image's bits</li>
        <li><strong>Decoder.py</strong>: Extracts message bits from image and converts them to text</li>
        <li><strong>main.py</strong>: User interface to run the full encode/decode process</li>
    </ul>

    <h2>How to Run</h2>
    <p>Run the following command in your terminal:</p>
    <pre><code>C:\Users\kpraj\PycharmProjects\ImageStrenography\.venv\Scripts\python.exe C:\Users\kpraj\PycharmProjects\ImageStrenography\main.py</code></pre>

    <h3>Example Console Interaction:</h3>
    <pre>
Enter the message: hello world!
Enter the image path: uwp4803195.png
Message encoded and saved as encoded_image.png
Decoded message from image: hello world!

Process finished with exit code 0
    </pre>

    <h2>Notes</h2>
    <ul>
        <li>The image must be in a compatible RGB format.</li>
        <li>The message size in bits must be less than or equal to the total number of bits in the image.</li>
        <li>The output encoded image is saved as <strong>encoded_image.png</strong> in the project directory.</li>
    </ul>

    <h2>Dependencies</h2>
    <ul>
        <li>Pillow</li>
        <li>NumPy</li>
    </ul>

    <h2>Install Dependencies</h2>
    <pre><code>pip install pillow numpy</code></pre>

    <h2>Author</h2>
    <p>Prajval — 2025</p>
