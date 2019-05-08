# Data
x_data = [2.0, 1.0, 3.0, -5.0]
y_data = [8.0, 4.0, 12.0, -20.0]

def forward(x, w):
    return x * w

def loss(y, y_pred):
    temp = (y - y_pred)
    return temp ** 2

if __name__ == '__main__':
    for w in range(0, 6):
        print('=====================')
        print('w=', 4 + w/10)

        l_sum = 0
        for x_val, y_val in zip(x_data, y_data):
            y_pred = forward(x_val, 4 + w/10)

            l = loss(y_val, y_pred)
            l_sum += l

            print('\t', x_val, y_val, y_pred)

        print('MSE={:3f}'.format(l_sum / 3))
