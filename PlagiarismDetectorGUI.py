import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QLabel, QVBoxLayout, QGraphicsView, QGraphicsScene
import PyQt5.QtGui as qtg
from fileparser import FileParser
from clusteranalyzer import ClusterAnalyzer

import pyqtPainter
class PlagiarismDetectorGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()




    def initUI(self):
        self.setWindowTitle('Plagiarism Detector')

        # Erstelle QGraphicsView-Objekt
        self.graphics_view = QGraphicsView()

        # Erstelle Szene für das QGraphicsView-Objekt
        self.scene = QGraphicsScene()
        self.graphics_view.setScene(self.scene)

        # Erstelle RainbowWidget-Objekt
        self.rainbow_widget = pyqtPainter.RainbowWidget()
        self.rainbow_widget.setGeometry(10, 10, 400, 400)
        self.scene.addWidget(self.rainbow_widget)

        self.selectFileButton1 = QPushButton('Datei 1 auswählen', self)
        self.selectFileButton1.clicked.connect(self.getFile1)
        self.selectFileButton1.setFont(qtg.QFont('Helvetica', 18))

        self.fileLabel1 = QLabel('Dateiname 1', self)
        self.fileLabel1.setFont(qtg.QFont('Helvetica', 18))

        self.selectFileButton2 = QPushButton('Datei 2 auswählen', self)
        self.selectFileButton2.clicked.connect(self.getFile2)
        self.selectFileButton2.setFont(qtg.QFont('Helvetica', 18))

        self.fileLabel2 = QLabel('Dateiname 2', self)
        self.fileLabel2.setFont(qtg.QFont('Helvetica', 18))

        self.checkButton = QPushButton('Überprüfen', self)
        self.checkButton.clicked.connect(self.checkPlagiarism)
        self.checkButton.setFont(qtg.QFont('Helvetica', 18))

        self.resultLabelTfidf = QLabel('Ergebnis Tfidf: ', self)
        self.resultLabelTfidf.setFont(qtg.QFont('Helvetica', 18))

        self.resultLabelCount = QLabel('Ergebnis Count: ', self)
        self.resultLabelCount.setFont(qtg.QFont('Helvetica', 18))

        vbox = QVBoxLayout()
        vbox.addWidget(self.graphics_view)

        vbox.addWidget(self.selectFileButton1)
        vbox.addWidget(self.fileLabel1)
        vbox.addWidget(self.selectFileButton2)
        vbox.addWidget(self.fileLabel2)
        vbox.addWidget(self.checkButton)
        vbox.addWidget(self.resultLabelTfidf)
        vbox.addWidget(self.resultLabelCount)


        self.setLayout(vbox)

        self.resize(600, 700)
        self.show()

    def getFile1(self):
        self.file1, _ = QFileDialog.getOpenFileName(self, "Datei 1 auswählen")
        if self.file1:
            print(f"Ausgewählte Datei 1: {self.file1}")
            self.fileLabel1.setText(f"{os.path.basename(self.file1)}")

    def getFile2(self):
        self.file2, _ = QFileDialog.getOpenFileName(self, "Datei 2 auswählen")
        if self.file2:
            print(f"Ausgewählte Datei 2: {self.file2}")
            self.fileLabel2.setText(f"{os.path.basename(self.file2)}")


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
        #plagiarism_score = analyzer.check_plagiarism(content1, content2)
        plagiarism_score = analyzer.check_plagiarism(tokens1, tokens2)


        # Ergebnis anzeigen
        self.resultLabelTfidf.setText(f"Plagiatswahrscheinlichkeit Tfidf: {plagiarism_score[0]}%")
        self.resultLabelCount.setText(f"Plagiatswahrscheinlichkeit Count: {plagiarism_score[1]}%")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PlagiarismDetectorGUI()
    sys.exit(app.exec_())
