import torch

def train(model, data, epoch, criterion, optimizer, device='cpu'):
    model.train()
    print('==========Train Epoch {}=========='.format(epoch))

    # >>>>>>>> Your turn <<<<<<<<<
    for i, (img, lbl) in enumerate(data):
        optimizer.zero_grad()

        pred_lbl = model(img)

        loss = criterion(pred_lbl, lbl)
        loss.backward()
        optimizer.step()

        if i % 300 == 0:
            print('epoch {} ({} / {}) loss: {}'.format(
                epoch, i, len(data),
                loss.item()
            ))
