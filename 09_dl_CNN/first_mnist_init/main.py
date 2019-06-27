import platform
import torch
#
from utils.dataset import train_data, test_data
from utils.model import SimpleCNN
from train import train
from test import test

if __name__ == '__main__':
    # == Model ==
    model = SimpleCNN()

    # == optimizer ==
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters())

    # == Main Loop ==
    max_epoch = 1
    for epoch in range(1, max_epoch + 1):
        train(model, train_data, epoch, criterion, optimizer)
        acc = test(model, test_data)
        print('Acc:', acc)

    torch.save(model.state_dict(), 'checkpoints/CNN_97.pt')
    #
