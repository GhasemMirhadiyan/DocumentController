import os


def GetFolderFile(f):
    file = f
    # splitFile = os.path.splitext(file)
    # extentionfile = splitFile[1]
    # if extentionfile == 'pdf':
    #     print(f'\n{file} is Pdf')
    # else:
    #     print(f'\n{file} is not Pdf')

    # checking if it is a file
    if os.path.isfile(file):
        return f



