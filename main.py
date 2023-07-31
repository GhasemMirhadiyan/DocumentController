import os

from ocrmypdf import ocr
import RegexChecking
import GetFile
import ReadFile
import autocad
import verification


def wellcome(name):
    print(f'{name}')


def Final():
    print(180 * '*')
    directory = 'E:\Project\output'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        file = GetFile.GetFolderFile(f)
        plaintext = ReadFile.ReadFile(file)
        #plaintext = ReadFile.ocr(file)
        #plaintext2 = ReadFile.ocrGithub(file)
        #print("Plaintext:", plaintext)
        tags = RegexChecking.TextProcess(plaintext, file)
        #print('\nTags:', tags)
        count, result, FileHoldTag = verification.verification(tags)
        print('Filename :', file)
        print("\nresult Before Checking:", "\nCounter:", len(tags), "\nTags:\n", result)
        print("Tags in One String Field and using for FileHold: \n", FileHoldTag)
        print(180 * '*')

        with open("E:\Project\Result\ListTags.txt", "a") as txtfile:
            txtfile.write(f'Filename: {file}\nLength:{len(result)}\nTags:\n{FileHoldTag}\n')
            txtfile.write(180*'*')

        TagsForFileHold = ''
        result = ''
        tags = ''


if __name__ == '__main__':
    autocad.dwg()
    Final()
    #ocr.ocrTest()
    #ReadFile.ocr()





