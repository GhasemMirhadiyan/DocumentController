import os
import aspose.cad as cad
import cad
import shutil


def dwg():
    directoryinput = 'E:\Project\input'
    directoryoutput = 'E:\Project\output'
    for filename in os.listdir(directoryinput):
        with open("E:\Project\Result\logs.txt", "a") as logfile:
            length = len(filename)
            # print(filename[length-4:length])
            if filename[length - 4:length] == '.dwg':
                cadfile = os.path.join(directoryinput, filename)
                # Load an existing DWG file
                image = cad.Image.load(cadfile)
                # Initialize and specify CAD options
                rasterizationOptions = cad.imageoptions.CadRasterizationOptions()
                rasterizationOptions.page_width = 1200
                rasterizationOptions.page_height = 1200
                # Specify PDF Options
                pdfOptions = cad.imageoptions.PdfOptions()
                pdfOptions.vector_rasterization_options = rasterizationOptions
                # Save as PDF
                name = directoryoutput + '\\' + filename[:-4] + '.pdf'
                image.save(name, pdfOptions)
                print(f"{filename} is DWG File  and Converting File to {directoryoutput}\n")
                logfile.write(f"{filename} :    Converted \n")
                logfile.write(120 * '*')
                logfile.write('\n')
            elif filename[length - 4:length] == '.pdf':
                #shutil.copyfile(directoryinput + '\\' + filename, directoryoutput + '\\' + filename)
                print(f"{filename} is pdffile and copy to {directoryoutput}\n")
                logfile.write(f"{filename} :    Copy.\n")
                logfile.write(120 * '*')
                logfile.write('\n')
            else:
                print(f'{filename} is not Recognize\n')
                logfile.write(f'{filename}     :    Not Recognized')
                logfile.write('\n')
                logfile.write(120 * '*')
                logfile.write('\n')
