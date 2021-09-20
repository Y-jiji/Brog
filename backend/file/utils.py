from os import path

FILE_PATH = path.join(__file__, "uploadedFile")

async def writeFile(fileName, content):
    with open(path.join(FILE_PATH, fileName), 'w') as f:
        f.write(content)