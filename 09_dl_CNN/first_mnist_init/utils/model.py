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
        pass

    def forward(self, x):
        pass
