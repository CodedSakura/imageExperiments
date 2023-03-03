from PIL import Image
from bitarray import bitarray

image = Image.open("res.png")
data = bitarray()

px = list(list(p) for p in image.getdata())

zero_count = 0

for i in range(len(px)):
    for v in range(len(px[i])):
        val = px[i][v] >> 7

        if val == 0:
            zero_count += 1
        else:
            zero_count = 0

        data.append(px[i][v] >> 7)

        px[i][v] &= 0b0111_1111
        px[i][v] <<= 1

        if zero_count == 16:
            break
    if zero_count == 16:
        break

print(data.tobytes()[:-2].decode("utf-8"))

image.putdata([tuple(p) for p in px])
image.show()
