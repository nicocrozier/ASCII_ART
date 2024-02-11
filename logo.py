from PIL import Image

# Load the image
img_path = 'aphex.jpg'  # Using your specified image path

try:
    img = Image.open(img_path)
except FileNotFoundError:
    print(f"Image not found at {img_path}")
    exit()

# Convert to grayscale
img = img.convert('L')

# Resize the image
aspect_ratio = img.width / img.height
new_width = 100  # You can change this width for different resolutions
new_height = int(new_width / aspect_ratio)

# Adjust for the aspect ratio of characters (characters are taller than they are wide)
char_aspect_ratio = 1.65  # Typical character aspect ratio in monospace font, adjust as needed
new_height = int(new_height / char_aspect_ratio)

img = img.resize((new_width, new_height))

# Extended ASCII characters (light to dark)
ascii_chars = ' .:=+*#%@/7A$'

# Map each pixel to an ASCII character
pixels = img.getdata()
ascii_str = '<pre style="font-family: monospace; line-height: 13.4px;">'
for i, pixel in enumerate(pixels):
    # Scale the pixel value to match the ascii_chars length
    index = (pixel * (len(ascii_chars) - 1)) // 255
    ascii_str += ascii_chars[index]
    if (i + 1) % new_width == 0:  # Ensure new line is added correctly
        ascii_str += '\n'
ascii_str += '</pre>'

# Save the ASCII art to an HTML file
with open('ascii_art.html', 'w') as file:
    file.write(ascii_str)

print("ASCII art saved to ascii_art.html")
