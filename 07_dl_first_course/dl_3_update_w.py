# Data
x_data = [2.0, 1.0, 3.0, -5.0]
y_data = [8.0, 4.0, 12.0, -20.0]

w = 1.0

def forward(x, w):
    return x * w

def loss(y, y_pred):
    temp = (y - y_pred)
    return temp ** 2

def gradient(x, y):
    return 2 * x * (x * w - y)

if __name__ == '__main__':
    for epoch in range(100):
        for x_val, y_val in zip(x_data, y_data):
            grad = gradient(x_val, y_val)

            # update weight
            w = w - 0.001 * grad

            y_pred = forward(x_val, w)
            l = loss(y_val, y_pred)

        if epoch % 10 == 0:
            print('Progress: ', epoch, 'w={:.2f}'.format(w), 'loss={:.2f}'.format(l))
    print('Predict(after training)', '4 hours', forward(4, w))
