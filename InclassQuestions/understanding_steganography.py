from steganography.steganography import Steganography


original_image = 'C:/Users/Burningdzire/Desktop/acadview/class/acadview/Death-Note-Anime.jpg'
output_path = 'output.jpg'
text = "Hello"
Steganography.encode(original_image, output_path, text)


output_path = input('What is the name of the file? ')
secret_text = Steganography.decode(output_path)