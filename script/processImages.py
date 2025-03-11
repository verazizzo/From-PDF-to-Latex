from .requestOpenAI import requestoOpenAI
import os
import base64 

def processImages(output_folders):
  responsesMap = {}

  for folder in output_folders:
    for image_file in os.listdir(folder):
      if image_file.endswith(".png"):
        image_path = os.path.join(folder, image_file)

        with open(image_path, "rb") as image:
          encoded_string =  base64.b64encode(image.read()).decode('utf-8')
        
        n_page = image_file.split(".")[0]

        response = requestoOpenAI(encoded_string, n_page)
        pdf_name = os.path.split(folder)[1] 

        if pdf_name in responsesMap:
          responsesMap[pdf_name].append(response.choices[0].message)
        else:
          responsesMap[pdf_name] = [response.choices[0].message]
        print(f"Saved response for the image: {image_file}")
  
  return responsesMap
