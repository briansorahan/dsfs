import math
import numpy  as np
import pandas as pd
import sys

from scipy.cluster.vq import vq, kmeans, whiten

def distance_from_centroid(centroid):
    return lambda pt: math.sqrt(math.pow(centroid[0] - pt[0], 2) +
                                math.pow(centroid[1] - pt[1], 2) +
                                math.pow(centroid[2] - pt[2], 2) +
                                math.pow(centroid[3] - pt[3], 2))

def get_closest(distances):
    return distances.idxmin()

def d_squared(distances):
    return math.pow(distances.min(), 2)
    
df       = pd.read_csv('un.csv.1')
clusters = []
k_range  = 10
whitened = whiten(df[['lifeMale', 'lifeFemale', 'infantMortality', 'GDPperCapita']].dropna())

print(whitened.dtype)

for i in range(k_range):
    codebook, distortion = kmeans(whitened, i+1)
    clusters.append({ 'size': i+1, 'codebook': codebook, 'distortion': distortion })

# Calculate the distance between each point and the centroids of each cluster.
features = df[['lifeMale', 'lifeFemale', 'infantMortality', 'GDPperCapita']].dropna()

# Probably want to use the whitened data to get meaningful results.
# Distances will be a M by k data frame.
for i in range(k_range):
    clusters[i]['distances'] = pd.DataFrame(index=features.index)
    for j in range(clusters[i]['size']):
        f = distance_from_centroid(clusters[i]['codebook'][j])
        # If I use features here instead of whitened,
        # they all cluster around the first centroid (for cluster 3)
        clusters[i]['distances']['d{}'.format(j+1)] = map(f, whitened)


for i in range(k_range):
    try:
        clusters[i]['distances'].drop(labels=['closest'], inplace=True, axis=1)
    except ValueError:
        pass
    clusters[i]['distances']['closest'] = clusters[i]['distances'].apply(func=get_closest, axis=1)
    clusters[i]['distances']['d_squared'] = clusters[i]['distances'].apply(func=d_squared, axis=1)

# Calculate average within-cluster sum of squares for each centroid.
wcss_averages = []
for i in range(k_range):
    wcss_averages.append(clusters[i]['distances'].pivot(columns='closest', values='d_squared').sum().mean())
