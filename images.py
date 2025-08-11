import os
from pdf2image import convert_from_path

# Set the path to your certificates folder and output folder
pdf_folder = 'certificates'  # relative to where you run the script
output_folder = os.path.join(pdf_folder, 'thumbnails')
poppler_path = r'C:\Users\kraja\Downloads\poppler-24.08.0\Library\bin'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(pdf_folder):
    if filename.lower().endswith('.pdf'):
        pdf_path = os.path.join(pdf_folder, filename)
        images = convert_from_path(pdf_path, dpi=100, first_page=1, last_page=1, poppler_path=poppler_path)
        if images:
            thumb_name = os.path.splitext(filename)[0] + '.png'
            thumb_path = os.path.join(output_folder, thumb_name)
            images[0].save(thumb_path, 'PNG')
            print(f"Generated thumbnail for {filename} -> {thumb_path}")