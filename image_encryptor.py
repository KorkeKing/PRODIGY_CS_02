from PIL import Image
import random

def encrypt_image(input_path, output_path, key):
    """
    Encrypts an image by shifting color values and scrambling pixel positions.
    Args:
        input_path (str): Path to the input image file
        output_path (str): Path to save the encrypted image
        key (int): Encryption key (used for both color shift and pixel shuffle)
    """
    img = Image.open(input_path).convert('RGB')
    pixels = list(img.getdata())

    # Step 1: Shift color values
    shifted_pixels = [((r + key) % 256, (g + key) % 256, (b + key) % 256) for (r, g, b) in pixels]

    # Step 2: Shuffle pixel positions
    random.seed(key)
    indices = list(range(len(shifted_pixels)))
    random.shuffle(indices)

    scrambled = [None] * len(shifted_pixels)
    for i, new_i in enumerate(indices):
        scrambled[new_i] = shifted_pixels[i]

    img.putdata(scrambled)
    img.save(output_path)
    print(f" Encrypted image saved as: {output_path}")


def decrypt_image(input_path, output_path, key):
    """
    Decrypts an image by reversing pixel position scrambling and color shifting.
    Args:
        input_path (str): Path to the encrypted image file
        output_path (str): Path to save the decrypted image
        key (int): Same key used for encryption
    """
    img = Image.open(input_path).convert('RGB')
    pixels = list(img.getdata())

    # Step 1: Reverse pixel position shuffle
    random.seed(key)
    indices = list(range(len(pixels)))
    random.shuffle(indices)

    unshuffled = [None] * len(pixels)
    for i, new_i in enumerate(indices):
        unshuffled[i] = pixels[new_i]

    # Step 2: Reverse color shift
    original_pixels = [((r - key) % 256, (g - key) % 256, (b - key) % 256) for (r, g, b) in unshuffled]

    img.putdata(original_pixels)
    img.save(output_path)
    print(f" Decrypted image saved as: {output_path}")
# using colab
# Encrypt the image
encrypt_image("sample.jpg", "encrypted.png", 128)

# Decrypt the image
decrypt_image("encrypted.png", "decrypted.png", 128)

