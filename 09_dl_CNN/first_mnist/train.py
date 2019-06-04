import torch

def train(model, data, epoch, criterion, optimizer, device='cpu'):
    model.train()
    print('==========Train Epoch {}=========='.format(epoch))

    for i, (image, label) in enumerate(data):
        image = image.to(device)
        label = label.to(device)

        optimizer.zero_grad()
        score = model(image) # predict the label
        loss = criterion(score, label) # calculate error
        loss.backward()  # back-propagation
        optimizer.step() # gradient descent

        if i % 300 == 0:
            print('epoch {} ({} / {}) loss: {}'.format(
                epoch, i, len(data),
                loss.item()
            ))

    # plt.plot(range(int(len(data) / 100) + 1), acc_list)
    # plt.show()
