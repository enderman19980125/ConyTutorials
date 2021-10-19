import numpy as np
import torch
import matplotlib.pyplot as plt
from torch.utils.data import TensorDataset, DataLoader
from torch import nn
from sklearn.metrics import accuracy_score


class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_1 = nn.Linear(2, 4)
        self.linear_2 = nn.Linear(4, 1)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.linear_1(x)
        x = self.relu(x)
        x = self.linear_2(x)
        return x


def generate_random_data(n: int, cx: float, cy: float):
    x = cx + np.random.randn(n)
    y = cy + np.random.randn(n)
    return x, y


def generate_data():
    x_array_1, y_array_1 = generate_random_data(10000, 10, 10)
    x_array_2, y_array_2 = generate_random_data(10000, 0, 0)
    x_array = np.concatenate((x_array_1, x_array_2), axis=None)
    y_array = np.concatenate((y_array_1, y_array_2), axis=None)
    xy_array = np.concatenate((x_array.reshape(-1, 1), y_array.reshape(-1, 1)), axis=1)
    label_array = np.concatenate((np.zeros(10000), np.ones(10000)), axis=None)
    # plt.scatter(x_array, y_array)
    # plt.show()

    xy_tensor = torch.Tensor(xy_array)
    label_tensor = torch.Tensor(label_array)

    return xy_tensor, label_tensor


if __name__ == '__main__':
    xy_tensor, label_tensor = generate_data()

    train_dataset = TensorDataset(xy_tensor, label_tensor)
    train_dataloader = DataLoader(train_dataset, batch_size=64, shuffle=True)

    model = NeuralNetwork()
    loss_fn = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

    model.train()
    for epoch_id in range(1, 10 + 1):

        for batch_id, (batch_data, batch_labels) in enumerate(train_dataloader):
            batch_predict = model(batch_data)
            loss = loss_fn(batch_predict.flatten(), batch_labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            batch_labels = [int(k) for k in batch_labels]
            batch_predict = [int(k + 0.5) for k in batch_predict]
            acc = accuracy_score(batch_labels, batch_predict)
            print(f'{epoch_id} {batch_id} {loss} {acc}')
