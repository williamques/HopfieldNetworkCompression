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

def average_pixels(imageData):
    newImageData = []
    for i in range(0, len(imageData), 2):
        new_row = []
        for j in range(0, len(imageData[i]), 2):
            pixels = [imageData[i][j], imageData[i][j + 1], imageData[i + 1][j], imageData[i + 1][j + 1]]
            average = sum(pixels) // 4
            new_row.append(average)
        newImageData.append(new_row)
    return newImageData

def write_pgm(fileName, width, height, maxVal, imageData):
    with open(fileName, 'wb') as f:
        f.write(b'P5\n')
        f.write(f"{width // 2} {height // 2}\n".encode())
        f.write(f"{maxVal}\n".encode())
        for row in imageData:
            for pixel in row:
                f.write(bytes([pixel]))

def compress_pgm(inputFileName, outputFileName):
    width, height, maxVal, imageData = read_pgm(inputFileName)
    newImageData = average_pixels(imageData)
    write_pgm(outputFileName, width, height, maxVal, newImageData)

for i in range(1, 21):
    inputFileName = f'image{i}.pgm'
    outputFileName = f'compressed_image{i}.pgm'
    compress_pgm(inputFileName, outputFileName)
