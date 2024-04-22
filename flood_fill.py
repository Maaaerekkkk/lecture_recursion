import matplotlib.pyplot as plt

def floodfill(img, x, y):

    if x >= img.shape[0] or y >= img.shape[1]:
        return img
    elif y < 0 or x < 0:
        return img
    elif img[x, y] == 0 or img[x, y] == 2:
        return img
    else:
        img[x,y] = 2
        floodfill(img, x + 1, y)
        floodfill(img, x - 1, y)
        floodfill(img, x, y + 1)
        floodfill(img, x, y - 1)
        return img




def main():
    # img = plt.imread("files/img0.png")[:, :, 0]
    # img = plt.imread("files/img1.png")[:, :, 0]
    img = plt.imread("files/img2.png")[:, :, 0]

    img = floodfill(img, 0, 0)

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()


if __name__ == "__main__":
    main()
