import os, platform
import torch
from PIL import Image
import numpy as np
from torchvision import transforms
#
import sys
sys.path.append('utils')
from utils.model import SimpleLinear, SimpleCNN
from plot import plot_with_label

def get_input_data(dir='input_data'):
    img_paths = [os.path.join(dir, p).replace('\\', '/') \
                    for p in os.listdir('./input_data') if '.png' in p]
    datas = []

    for p in img_paths:
        data = Image.open(p).convert('L')
        data = transforms.ToTensor()(data)
        data = abs(data - 1)

        data = data.unsqueeze(0)
        datas.append(data)

    imgs = torch.cat(datas)
    print(imgs.shape)
    return imgs

if __name__ == '__main__':
    # == Setting ==
    if platform.system() == 'Windows':
        device = torch.device('cuda')
    else:
        device = torch.device('cpu')
    print(device)

    # == Model ==
    model_files = 'checkpoints/best_CNN_99.pt'
    model = SimpleCNN()
    model.load_state_dict(torch.load(model_files, map_location='cpu'))
    model = model.to(device)

    # == Data ==
    imgs = get_input_data()

    # == Apply ==
    model.eval()

    out = model(imgs)

    out_labels = torch.argmax(out, dim=1)
    plot_with_label(imgs, out_labels,
            batch_size=out.size(0), rows=2, cols=3)
