from pdf2image import convert_from_path
import os
import glob

def convertPDFtoPNG():
  poppler_path='script/poppler-24.08.0/Library/bin'
  pdfs = glob.glob(os.path.join("inputFiles", "*.pdf"))
  output_folders = []

  for pdf_file in pdfs:
    pdf_name = os.path.splitext(os.path.basename(pdf_file))[0]
    output_folder = os.path.join("tempFiles", f"{pdf_name}")

    if not os.path.exists(output_folder):

      images = convert_from_path(pdf_file, 500, poppler_path=poppler_path)

      os.makedirs(output_folder)

      for i, image in enumerate(images):
        fname = os.path.join(output_folder, f'{i+1}.png')
        image.save(fname, "PNG")

    output_folders.append(output_folder)
    
  print("tempFiles created")
    
  return output_folders

convertPDFtoPNG()