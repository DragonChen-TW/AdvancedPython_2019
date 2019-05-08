import torch
from torch.autograd import Variable

x_data = Variable(torch.Tensor([[2.0], [-1.0], [3.0], [-5.0]]))
y_data = Variable(torch.Tensor([[-4.0], [2.0], [-6.0], [10.0]]))

class LinearModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)
        # 1 is input size, 1 is output size

    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred

if __name__ == '__main__':
    model = LinearModel()

    # criterion = torch.nn.MSELoss(reduction='elementwise_mean')
    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

    for epoch in range(50):
        # Forward
        y_pred = model(x_data)

        # Compute and print loss
        loss = criterion(y_pred, y_data)
        # print(epoch, loss.item())

        # Zero gradients, backward
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if epoch % 5 == 0:
            hour_var = Variable(torch.Tensor([[4.0]]))
            print('Predict: ', 4, model.forward(hour_var).data)


    # # After Training
    # hour_var = Variable(torch.Tensor([[4.0]]))
    # print('Predict(after training): ', 4, model.forward(hour_var).data)
