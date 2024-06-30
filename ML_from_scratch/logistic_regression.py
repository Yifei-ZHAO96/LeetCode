import numpy as np


def l1_grad(W):
    if W > 0:
        return 1
    elif W < 0:
        return -1
    else:
        return 0

def l1_norm(W):
    return np.sum(abs(W))

def l2_grad(W):
    return 2 * W

def l2_norm(W):
    return np.sum(W ** 2)

def sigmod(x):
    return 1 / (1 + np.exp(-x))

def initialize(dim):
    W = np.zeros((dim, 1))
    b = 0
    return W, b

def logistic_loss(X, y, W, b, alpha=0, norm=None):
    num_data = X.shape[0]
    norm_term = 0
    norm_grad = 0
    if norm == 'l1':
        norm_term = alpha * l1_norm(W)
        norm_grad = alpha * np.vectorize(l1_grad)(W)
    elif norm == 'l2':
        norm_term = alpha * l2_norm(W)
        norm_grad = alpha * l2_grad(W)
    
    y_hat = sigmod(np.dot(X, W) + b)
    loss = -1 / num_data * np.sum(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat)) + norm_term
    loss = np.squeeze(loss)
    dW = np.dot(X.T, (y_hat - y)) / num_data + norm_grad
    db = np.sum(y_hat - y) / num_data
    
    return loss, dW, db

def train(X, y, lr, epochs, alpha, norm):
    W, b = initialize(X.shape[1])
    loss_list = []
    
    for e in range(1, epochs + 1):
        loss, dW, db = logistic_loss(X, y, W, b, alpha, norm)
        loss_list.append(loss)
        W -= lr * dW
        b -= lr * db
        
        if e % 1000 == 0:
            print('epoch {} loss {}'.format(e, loss))
        
    params = {
        'W': W,
        'b': b
    }
        
    grads = {
        'dw': dW,
        'db': db
    }
    return loss_list, params, grads

def predict(X, params):
    return np.round(sigmod(np.dot(X, params['W'] + params['b'])))

def accuracy(y_pred, y):
    count = 0
    for i in range(len(y_pred)):
        if y_pred[i] == y[i]:
            count += 1
    
    return count / len(y_pred)

def plot_logistic(X, y, params):
    n = X.shape[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):        
        if y[i] == 1:
            xcord1.append(X[i][0])
            ycord1.append(X[i][1])        
        else:
            xcord2.append(X[i][0])
            ycord2.append(X[i][1])
        
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1,s=32, c='red')
    ax.scatter(xcord2, ycord2, s=32, c='green')
    x = np.arange(-1.5, 3, 0.1)
    y_hat = (-params['b'] - params['W'][0] * x) / params['W'][1]
    ax.plot(x, y_hat)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()

if __name__ == '__main__':
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    
    X, y = make_classification(n_samples=1000, n_features=10, n_informative=8, n_clusters_per_class=2)
    y = y.reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    X_train = X_train.astype(np.float32)
    X_test = X_test.astype(np.float32)
    
    loss_list, params, grads = train(X_train, y_train, 0.001, 10000, alpha=0.1, norm='l2')
    print("params:", params)
    
    # testing
    y_hat = predict(X_test, params)
    print("accuracy:", accuracy(y_hat, y_test))

    # visualization
    import matplotlib.pyplot as plt
    plot_logistic(X, y, params)
    plt.plot(loss_list)
    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.show()