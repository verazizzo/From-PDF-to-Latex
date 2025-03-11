from script.convertPDFtoPNG import convertPDFtoPNG
from script.processImages import processImages
from script.createResponsesTXT import createResponsesTXT


output_folders = convertPDFtoPNG()
responsesMap = processImages(output_folders) 
createResponsesTXT(responsesMap)
