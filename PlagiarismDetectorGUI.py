import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QLabel, QVBoxLayout
from fileparser import FileParser
from clusteranalyzer import ClusterAnalyzer
class PlagiarismDetectorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Plagiarism Detector')

        self.selectFileButton1 = QPushButton('Datei 1 auswählen', self)
        self.selectFileButton1.clicked.connect(self.getFile1)

        self.selectFileButton2 = QPushButton('Datei 2 auswählen', self)
        self.selectFileButton2.clicked.connect(self.getFile2)

        self.checkButton = QPushButton('Überprüfen', self)
        self.checkButton.clicked.connect(self.checkPlagiarism)

        self.resultLabel = QLabel('Ergebnis: ', self)

        self.similarity_options = ["Jaccard Index", "Rand Index"]
        self.similarity_menu = QComboBox(self)
        self.similarity_menu.addItems(self.similarity_options)

        self.clustering_options = ["KMeans", "Agglomeratives Clustering"]
        self.clustering_menu = QComboBox(self)
        self.clustering_menu.addItems(self.clustering_options)


        vbox = QVBoxLayout()
        vbox.addWidget(self.selectFileButton1)
        vbox.addWidget(self.selectFileButton2)
        vbox.addWidget(self.checkButton)
        vbox.addWidget(self.resultLabel)
        vbox.addWidget(self.similarity_menu)
        vbox.addWidget(self.clustering_menu)

        self.setLayout(vbox)
        self.show()

    def getFile1(self):
        self.file1, _ = QFileDialog.getOpenFileName(self, "Datei 1 auswählen")
        if self.file1:
            print(f"Ausgewählte Datei 1: {self.file1}")
        # Hier können Sie den Code zum Umgang mit der ausgewählten Datei hinzufügen

    def getFile2(self):
        self.file2, _ = QFileDialog.getOpenFileName(self, "Datei 2 auswählen")
        if self.file2:
            print(f"Ausgewählte Datei 2: {self.file2}")
        # Hier können Sie den Code zum Umgang mit der ausgewählten Datei hinzufügen


    def checkPlagiarism(self):

        # Dateien einlesen
        parser1 = FileParser(self.file1)
        content1 = parser1.read_file()

        parser2 = FileParser(self.file2)
        content2 = parser2.read_file()

        # Tokenisieren
        tokens1 = parser1.tokenize(content1)
        tokens2 = parser2.tokenize(content2)

        # Clusteranalyse
        analyzer = ClusterAnalyzer()
        plagiarism_score = analyzer.check_plagiarism(tokens1, tokens2)

        # Ergebnis anzeigen
        self.resultLabel.setText(f"Plagiatswahrscheinlichkeit: {plagiarism_score}%")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PlagiarismDetectorGUI()
    sys.exit(app.exec_())
