import numpy as np


def k_means(X, K, iter=500, tol=1e-4):
    centriods = X[np.random.choice(X.shape[0], K, replace=False)]

    for _ in range(iter):
        dist = np.sqrt(((X[:, np.newaxis] - centriods) ** 2).sum(axis=2))
        centriods_ids = np.argmin(dist, axis=1)
        centriods = np.array([X[centriods_ids == i].mean(axis=0)
                             for i in range(K)])

    return centriods, centriods_ids


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    X = np.concatenate([np.random.normal(1, scale=1, size=(100, 2)),
                        np.random.normal(5, scale=1, size=(100, 2)),
                        np.random.normal(9, scale=1, size=(100, 2)),
                        ], axis=0)
    print(X.shape)
    centroids, idx = k_means(X, 3)
    plt.scatter(X[:, 0], X[:, 1], c=idx)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X')
    plt.show()
