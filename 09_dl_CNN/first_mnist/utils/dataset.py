from torch.utils.data import Dataset, DataLoader
from torchvision import datasets, transforms

dir = '~/data/'
# dir = 'D:/data/'
batch_size = 16

dataset_train = datasets.MNIST(root=dir, train=True,
                            transform=transforms.ToTensor(),
                            download=True)
dataset_test = datasets.MNIST(root=dir, train=False,
                            transform=transforms.ToTensor(),
                            download=True)

train_data = DataLoader(dataset=dataset_train,
                          batch_size=batch_size,
                          shuffle=True)
test_data = DataLoader(dataset=dataset_test,
                         batch_size=batch_size,
                         shuffle=False)

if __name__ == '__main__':
    from plot import plot_with_label

    images, labels = iter(train_data).next()
    plot_with_label(images, labels)
