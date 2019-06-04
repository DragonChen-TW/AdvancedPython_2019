import matplotlib.pyplot as plt

def plot_with_label(images, labels, batch_size=16, rows=4, cols=4):
    images = images.squeeze() # 16x28x28

    for i in range(batch_size):
        plt.subplot(rows, cols, i + 1) # 1 ~ 4
        plt.imshow(images[i,:,:].numpy(), cmap='gray')
        plt.title(labels[i].item())
        plt.axis('off')
    plt.show()
