from torch import nn
import torch.nn.functional as F

class SimpleLinear(nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = nn.Linear(784, 530)
        self.l2 = nn.Linear(530, 410)
        self.l3 = nn.Linear(410, 290)
        self.l4 = nn.Linear(290, 150)
        self.l5 = nn.Linear(150, 10)

    def forward(self, x):
        # reshape (n, 1, 28, 28) to (n, 784)
        x = x.view(-1, 784)
        x = F.relu(self.l1(x))
        x = F.relu(self.l2(x))
        x = F.relu(self.l3(x))
        x = F.relu(self.l4(x))
        return self.l5(x)

class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.mp = nn.MaxPool2d(2)
        self.fc = nn.Linear(320, 10)

    def forward(self, x):
        in_size = x.size(0)

        x = self.mp(self.conv1(x))
        x = F.relu(x)
        x = self.mp(self.conv2(x))
        x = F.relu(x)
        x = x.view(in_size, -1)
        x = self.fc(x)

        return x
