def read_pgm(fileName):
    with open(fileName, 'rb') as f:
        header = f.readline()
        width, height = map(int, f.readline().split())
        maxVal = int(f.readline().strip())
        imageData = []
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(int.from_bytes(f.read(1), 'big'))
            imageData.append(row)
    return width, height, maxVal, imageData

def write_pgm(fileName, width, height, maxVal, imageData):
    with open(fileName, 'wb') as f:
        f.write(b'P5\n')
        f.write(f"{width} {height}\n".encode())
        f.write(f"{maxVal}\n".encode())
        for row in imageData:
            for pixel in row:
                f.write(bytes([pixel]))

def expand_pixels(imageData):
    newImageData = []
    for i in range(len(imageData)):
        newRow = []
        for j in range(len(imageData[i])):
            pixel = imageData[i][j]
            newRow.extend([pixel, pixel])
        newImageData.extend([newRow.copy(), newRow.copy()])
    return newImageData

def expand_pgm(inputFileName, outputFileName):
    width, height, maxVal, imageData = read_pgm(inputFileName)
    newWidth = width * 2
    newHeight = height * 2
    newImageData = expand_pixels(imageData)
    write_pgm(outputFileName, newWidth, newHeight, maxVal, newImageData)

for i in range(1, 21):
    inputFileName = f'compressed_image{i}.pgm'
    outputFileName = f'expanded_image{i}.pgm'
    expand_pgm(inputFileName, outputFileName)
