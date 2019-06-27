import platform
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from dl_plot import plot_with_label

if platform.system() == 'Windows':
    dir = 'D:/data/'
else:
    dir = '~/data/'
print('dir in', dir)

batch_size = 16

# Dataset
dataset_train = datasets.MNIST(root=dir, train=True,
                            transform=transforms.ToTensor(),
                            download=True)
dataset_test = datasets.MNIST(root=dir, train=False,
                            transform=transforms.ToTensor(),
                            download=True)

# DataLoader
train_data = DataLoader(dataset=dataset_train,
                          batch_size=batch_size,
                          shuffle=True)
test_data = DataLoader(dataset=dataset_test,
                         batch_size=batch_size,
                         shuffle=False)


if __name__ == '__main__':
    for i, data in enumerate(train_data):
        images, labels = data
        # images 16x1x28x28
        # labels 16x1
        break
    # or combine
    # for i, (images, labels) in enumerate(train_data):

    plot_with_label(images, labels)
