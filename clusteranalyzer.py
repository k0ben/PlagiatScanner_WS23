import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity



class ClusterAnalyzer:

    def __init__(self, n_clusters=2, n_init=10):
        self.n_clusters = n_clusters
        self.n_init = n_init
        self.vectorizer = TfidfVectorizer()
        self.kmeans = KMeans(n_clusters=self.n_clusters, n_init=self.n_init)

    def tfidf_vectorize(self, tokens1, tokens2):
        tfidf_matrix = self.vectorizer.fit_transform([tokens1, tokens2])
        return tfidf_matrix

    def count_vectorize(self, tokens1, tokens2):
        count_matrix = CountVectorizer().fit_transform([tokens1, tokens2])
        return count_matrix

    def cluster_centers(self, matrix):
        clusters = self.kmeans.fit(matrix)
        centroids = clusters.cluster_centers_
        return centroids

    def check_plagiarism(self, tokens1, tokens2):
        sparse_matrix_tfidf = self.tfidf_vectorize(tokens1, tokens2)
        sparse_matrix_count = self.count_vectorize(tokens1, tokens2)

        centroids_tfidf = self.cluster_centers(sparse_matrix_tfidf)
        centroids_count = self.cluster_centers(sparse_matrix_count)

        percent_tfidf = self.calculate_score(centroids_tfidf)
        percent_count = self.calculate_score(centroids_count)

        scores = [percent_tfidf, percent_count]
        return scores

    def calculate_score(self, centroids):
        similarity = cosine_similarity(centroids)

        score = "%.2f" % (similarity[1][0] * 100)

        return score