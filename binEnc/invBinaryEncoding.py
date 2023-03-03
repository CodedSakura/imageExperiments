from PIL import Image
from bitarray import bitarray

image = Image.open("../test512.png")
# image = Image.new("RGB", (512, 512), (0, 0, 0))
px = list([list(p) for p in image.getdata()])

with open("../testData.txt", "br") as f:
    bits = bitarray()
    bits.fromfile(f)


def process_value(index, value):
    if index >= len(bits):
        return value

    target_val = bits[index]
    value >>= 1
    value |= target_val << 7
    return value


imageIndex = 0
bitIndex = 0
while imageIndex < len(px):
    for k, v in enumerate(px[imageIndex]):
        px[imageIndex][k] = process_value(bitIndex, v)
        bitIndex += 1
    imageIndex += 1

image.putdata([tuple(p) for p in px])
image.save("res.png")
