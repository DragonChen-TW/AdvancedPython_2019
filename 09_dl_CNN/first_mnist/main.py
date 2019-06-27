import platform
import torch
#
from utils.dataset import train_data, test_data
from utils.model import SimpleLinear, SimpleCNN
from train import train
from test import test

if __name__ == '__main__':
    # == Setting ==
    device = torch.device('cpu')

    # == Model ==
    model = SimpleCNN()
    model = model.to(device)

    # == optimizer ==
    criterion = torch.nn.CrossEntropyLoss().to(device)
    optimizer = torch.optim.Adam(model.parameters())

    # == Main Loop ==
    max_acc = 0
    max_epoch = 1

    # first epoch
    # test(model, test_data, device=device)

    for epoch in range(1, max_epoch + 1):
        train(model, train_data, epoch, criterion, optimizer, device=device)
        acc = test(model, test_data, device=device)
        if acc > max_acc:
            max_acc = acc
            torch.save(model.state_dict(), 'checkpoints/best_model.pt')

    print('==========Max Acc: {}=========='.format(max_acc))
