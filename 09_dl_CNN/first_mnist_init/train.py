import torch

def train(model, data, epoch, criterion, optimizer, device='cpu'):
    model.train()
    print('==========Train Epoch {}=========='.format(epoch))

    # >>>>>>>> Your turn <<<<<<<<<
