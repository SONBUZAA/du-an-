import numpy as np

def correlation(img, kernel):
    img_height = img.shape[0]
    img_width = img.shape[1]
    kernel_height = kernel.shape[0]
    kernel_width = kernel.shape[1]
    H = (kernel_height - 1) // 2
    W = (kernel_width - 1) // 2
    out = np.zeros((img_height, img_width))
    
    # Lật mặt nạ theo cả hai trục ngang và dọc
    flipped_kernel = np.flipud(np.fliplr(kernel))
    
    for i in np.arange(H, img_height - H):
        for j in np.arange(W, img_width - W):
            sum = 0
            for k in np.arange(-H, H + 1):
                for l in np.arange(-W, W + 1):
                    a = img[i + k, j + l]
                    w = flipped_kernel[H + k, W + l]
                    sum += (w * a)
            out[i, j] = sum
    return out

in_img = np.array([[1, 0, 0, 1, 0],
                   [0, 1, 1, 0, 1],
                   [1, 0, 1, 0, 1],
                   [1, 0, 0, 1, 1],
                   [0, 1, 1, 0, 1]])

kernel = np.array([[1, 0, 0],
                   [0, 1, 1],
                   [1, 0, 1]])

out_img = correlation(in_img, kernel)
with np.printoptions(suppress=True):
    print(out_img)
