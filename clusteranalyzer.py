import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


class ClusterAnalyzer:

    def __init__(self, n_clusters=2, n_init=10):
        self.n_clusters = n_clusters
        self.n_init = n_init
        self.vectorizer = TfidfVectorizer()
        self.kmeans = KMeans(n_clusters=self.n_clusters, n_init=self.n_init)

    def vectorize(self, tokens):
        tfidf_matrix = self.vectorizer.fit_transform(tokens)
        return tfidf_matrix

    def cluster(self, vectorized_tokens):
        self.kmeans.fit(vectorized_tokens)
        clusters = self.kmeans.labels_
        return clusters

    def create_contingency_matrix(self, clusters1, clusters2):
        """Create contingency matrix between two cluster assignments"""

        n_clusters = max(clusters1.max(), clusters2.max()) + 1

        matrix = np.zeros((n_clusters, n_clusters))

        for i in range(len(clusters1)):
            matrix[clusters1[i], clusters2[i]] += 1

        return matrix

    def check_plagiarism(self, tokens1, tokens2):
        vec_tokens1 = self.vectorize(tokens1)
        vec_tokens2 = self.vectorize(tokens2)

        clusters1 = self.cluster(vec_tokens1)
        clusters2 = self.cluster(vec_tokens2)

        score = self.calculate_score(clusters1, clusters2)
        return score * 100

    def calculate_score(self, clusters1, clusters2):
        contingency_matrix = self.create_contingency_matrix(clusters1, clusters2)

        num_matches = np.trace(contingency_matrix)
        num_samples = np.sum(contingency_matrix)

        score = num_matches / num_samples

        return score


