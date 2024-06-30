import numpy as np


# https://mp.weixin.qq.com/s?__biz=MzI4ODY2NjYzMQ==&mid=2247485411&idx=2&sn=ff3af2ecba5b4beb316b0a1c6fa69a01&chksm=ec3ba28bdb4c2b9d2ab137981508a2c6a1363650e23676d74daa65afe40312aec06faa1549cc&scene=21#wechat_redirect
def l1_grad(w):
    """
    sign function
    """
    if w > 0:
        return 1
    elif w < 0:
        return -1
    else:
        return 0


def l1_norm(W):
    """
    np.sum(||W||)
    """
    return np.sum(abs(W))

# https://mp.weixin.qq.com/s?__biz=MzI4ODY2NjYzMQ==&mid=2247485421&idx=1&sn=e049abc5f02b6516f0d7e7206b2775ef&chksm=ec3ba285db4c2b93fc507b5be021126d21b87c3d500e80a5bd59f49d4bd7131f98d10ae1dd5a&scene=21#wechat_redirect


def l2_grad(w):
    """
    2 * W
    """
    return 2 * w


def l2_norm(W):
    """
    np.sum(||W ** 2||)
    """
    return np.sum(W ** 2)

# http://mp.weixin.qq.com/s?__biz=MzI4ODY2NjYzMQ==&mid=2247484471&idx=1&sn=c90b4917c5d6dd4d2b785ad18f2c6f1f&chksm=ec3ba15fdb4c28497cfd9cb935f3bec185104ef9dc096ca20f6a5853cc6506d992ffa6086b0b&scene=21#wechat_redirect


def linear_loss(X, y, W, b, alpha=0, norm=None):
    """
    y_hat = X * W + b
    loss = np.sum((y_hat - y) ** 2) / len(X)
    dw = X.T * (y_hat - y)
    db = y_hat - y

    Args:
        X: num_train * num_feature
        y: num_train * 1
        w: num_feature * 1
        b: 1
        alpha: normalization coefficient
        norm: normalization type
    """
    num_data = X.shape[0]
    norm_term = 0
    norm_grad = 0

    if norm == 'l1':
        norm_term = alpha * l1_norm(W)
        norm_grad = alpha * np.vectorize(l1_grad)(W)

    elif norm == 'l2':
        norm_term = alpha * l2_norm(W)
        norm_grad = alpha * l2_grad(W)

    y_hat = np.dot(X, W) + b
    loss = np.sum((y_hat - y) ** 2) / num_data + norm_term

    dw = np.dot(X.T, (y_hat - y)) / num_data + norm_grad
    db = np.sum(y_hat - y) / num_data
    return loss, dw, db


def initialize(dim):
    W = np.zeros((dim, 1))
    b = 0
    return W, b


def train(X, y, lr, epochs, alpha=0, norm=None):
    W, b = initialize(X.shape[1])
    loss_list = []

    for e in range(1, epochs + 1):
        loss, dw, db = linear_loss(X, y, W, b, alpha, norm)
        loss_list.append(loss)
        W -= lr * dw
        b -= lr * db

        if e % 1000 == 0:
            print('epoch {} loss {}'.format(e, loss))

    params = {
        'W': W,
        'b': b
    }

    grads = {
        'dw': dw,
        'db': db
    }
    return loss_list, params, grads


def predict(X, paras):
    return np.dot(X, paras['W']) + paras['b']


if __name__ == '__main__':
    from sklearn.datasets import make_regression
    from sklearn.model_selection import train_test_split

    X, y = make_regression(n_samples=1000, n_features=10,
                           n_informative=8, noise=20)
    y = y.reshape(-1, 1)
    print(X.shape, y.shape)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    X_train = X_train.astype(np.float32)
    X_test = X_test.astype(np.float32)

    # training
    loss_list, params, grads = train(
        X_train, y_train, 0.001, 10000, alpha=0.1, norm='l1')
    print("params:", params)

    # testing
    y_hat = predict(X_test, params)
    print()

    # visualization
    import matplotlib.pyplot as plt
    f = X_test.dot(params['W']) + params['b']
    plt.scatter(range(X_test.shape[0]), y_test)
    plt.plot(f, color='darkorange')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.show()

    plt.plot(loss_list)
    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.show()
