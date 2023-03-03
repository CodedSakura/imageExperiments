from PIL import Image

image = Image.open("../test512.png")
# image = Image.new("RGB", (512, 512), (0, 0, 0))
px = list([list(p) for p in image.getdata()])

for i in range(len(px)):
    for v in range(len(px[i])):
        p = px[i][v]
        px[i][v] = (((p >> 7 & 1) << 4) |
                    ((p >> 6 & 1) << 5) |
                    ((p >> 5 & 1) << 6) |
                    ((p >> 4 & 1) << 7) |
                    ((p >> 3 & 1) << 3) |
                    ((p >> 2 & 1) << 2) |
                    ((p >> 1 & 1) << 1) |
                    ((p >> 0 & 1) << 0) |
                    0)

image.putdata([tuple(p) for p in px])
image.save("out.png")
