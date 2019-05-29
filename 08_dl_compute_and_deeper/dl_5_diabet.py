import torch
from torch.autograd import Variable
import numpy as np

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = torch.nn.Linear(8, 6)
        self.l2 = torch.nn.Linear(6, 4)
        self.l3 = torch.nn.Linear(4, 1)

        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        out1 = self.sigmoid(self.l1(x))
        out2 = self.sigmoid(self.l2(out1))
        y_pred = self.sigmoid(self.l3(out2))

        return y_pred


if __name__ == '__main__':
    # Load data
    xy = np.loadtxt('./data/diabetes.csv', delimiter=',', dtype=np.float32)
    x_data = Variable(torch.from_numpy(xy[:, 0:-1]))
    y_data = Variable(torch.from_numpy(xy[:, [-1]]))

    # Build Model
    model = Model()

    # Decide
    # criterion = torch.nn.BCELoss(reduction='elementwise_mean')
    criterion = torch.nn.BCELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

    # Training
    for epoch in range(300):
        y_pred = model(x_data)

        loss = criterion(y_pred, y_data)
        if epoch % 5 == 0:
            print(epoch, loss.item())

        # zero gradient perform a backward, update weight
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
