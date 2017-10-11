import numpy as np
import matplotlib.pyplot as plt
import csv
from itertools import islice

def cluster_content(X, mu):
    cluster = {}
    for x in X:
        value = min([(i[0], np.linalg.norm(x - mu[i[0]])) for i in enumerate(mu)], key=lambda s: s[1])[0]
        try:
            cluster[value].append(x)
        except:
            cluster[value] = [x]
    return cluster

def new_center(mu, cluster):
    keys = sorted(cluster.keys())
    newmu = np.array([(np.mean(cluster[k], axis=0)) for k in keys])
    return newmu

def matched(nmu, omu):
    return (set([tuple(a) for a in nmu]) == set([tuple(a) for a in omu]))

def Apply_Kmeans(X, K, N):
    t1 = np.random.randint(N, size=K)
    omu = np.array([X[i] for i in t1])
    t2 = np.random.randint(N, size=K)
    nmu = np.array([X[i] for i in t2])
    cluster = cluster_content(X, omu)
    itr = 0
    plot_cluster(omu, cluster, itr)
    while not matched(nmu, omu):
        itr = itr + 1
        omu = nmu
        cluster = cluster_content(X, nmu)
        plot_cluster(nmu, cluster, itr)
        nmu = new_center(nmu, cluster)
    plot_cluster(nmu, cluster, itr)
    return

def plot_cluster(mu, cluster, itr):
    color = 10 * ['r.', 'g.', 'k.', 'c.', 'b.', 'm.']
    print('Iteration number : ', itr)
    for l in cluster.keys():
        for m in range(len(cluster[l])):
            plt.plot(cluster[l][m][0], cluster[l][m][1], color[l], markersize=10)
    plt.scatter(mu[:, 0], mu[:, 1], marker='x', s=150, linewidths=5, zorder=10)
    plt.show()

def get_data():
    csv_reader = csv.reader(open('Customers.csv'))
    a = []
    N = 0
    for row in islice(csv_reader, 1, None):
        a.append([int(row[2]), int(row[3])])
        N = N + 1
    X = np.array(a)
    return X

def Simulate_Clusters():
    csv_reader = csv.reader(open('Customers.csv'))

    N = 0
    for row in islice(csv_reader, 1, None):

        N = N + 1
    K = 5
    X = get_data()
    plt.scatter(X[:, 0], X[:, 1])  #
    plt.show()
    temp = Apply_Kmeans(X, K, N)

if __name__ == '__main__':
    Simulate_Clusters()