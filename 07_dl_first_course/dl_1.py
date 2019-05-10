import torch # someone would using shortcut

# torch.Tensor is basic unit
# like numpy in Deep Learning

# init Tensor
t1 = torch.Tensor([3.0, 2.5, -7.2])
print(t1)

# transpose tensor
t2 = torch.Tensor([[1, 3, 5], [-2, -4, -6]])
print(t2.shape)

# transpose
print(t2.t())

# Loss Function
l = torch.nn.MSELoss()            # Mean Square Loss
l = torch.nn.CrossEntropyLoss()   # Cross Entropy Loss
