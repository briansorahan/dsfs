import numpy  as np
import pandas as pd

from scipy.cluster.vq import vq, kmeans, whiten

df       = pd.read_csv('un.csv.1')
whitened = whiten(df[['lifeMale', 'lifeFemale', 'infantMortality', 'GDPperCapita']].dropna())
features = df[['lifeMale', 'lifeFemale', 'infantMortality', 'GDPperCapita']].dropna()

# We see the biggest drops in average wcss between 1 and 2, and 2 and 3.
# Now we use kmeans with a cluster size of 3.
cluster_size         = 3
distances            = pd.DataFrame(index=features.index)
codebook, distortion = kmeans(whitened, cluster_size)

for i in range(cluster_size):
    f = distance_from_centroid(codebook[i])
    distances['d{}'.format(i+1)] = map(f, whitened)

features['closest'] = distances.idxmin(axis=1)

print(features)

# colors = { 'd1': 0, 'd2': 0.5, 'd3': 1 }
# features['color'] = map(lambda c: colors[c], features['closest'])

# features.plot(kind='scatter', x='GDPperCapita', y='infantMortality', c='color', colormap='spectral')
# features.plot(kind='scatter', x='GDPperCapita', y='lifeMale', c='color', colormap='spectral')
# features.plot(kind='scatter', x='GDPperCapita', y='lifeFemale', c='color', colormap='spectral')
