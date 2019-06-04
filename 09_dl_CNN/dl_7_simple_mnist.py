from torch import nn
import torch.nn.functional as F

class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.mp = nn.MaxPool2d(2)
        self.fc = nn.Linear(320, 10)

    def forward(self, x):
        in_size = x.size(0)
        # the number of batch_size not the shape of img

        x = self.mp(self.conv1(x))
        x = F.relu(x)
        # conv2 1x28x28 > 10x24x24
        # max_pool 10x24x24 > 10x12x12

        x = self.mp(self.conv2(x))
        x = F.relu(x)
        # conv2 10x12x12 > 20x8x8
        # max_pool 20x8x8 > 20x4x4

        x = x.view(in_size, -1) # flatten the tensor
        x = self.fc(x)

        return x
