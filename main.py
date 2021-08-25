from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore 
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import screen2


class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("NISANDIGDHAK")
        self.setFixedSize(950,700)
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Home Page")
        self.label.move(25,50)
        self.label.setFixedSize(900,500)
        self.label.setStyleSheet('''
            border: 3px inset black;
            padding: 20px;
        ''')
        self.label.setAlignment(QtCore.Qt.AlignLeft)
        self.home()

        self.homeButton = QtWidgets.QPushButton(self)
        self.homeButton.setText("Home")
        self.homeButton.move(0,0)
        self.homeButton.clicked.connect(self.home)

        self.helpButton = QtWidgets.QPushButton(self)
        self.helpButton.setText("Help")
        self.helpButton.move(100,0)
        self.helpButton.clicked.connect(self.help)

        self.aboutButton = QtWidgets.QPushButton(self)
        self.aboutButton.setText("About")
        self.aboutButton.move(200,0)
        self.aboutButton.clicked.connect(self.about)

        self.startButton = QtWidgets.QPushButton(self)
        self.startButton.setText("START")
        self.startButton.setStyleSheet("""
            font-weight:bold;
        """)
        self.startButton.setFixedSize(100, 50)
        self.startButton.setFont(QFont('Arial', 10))
        self.startButton.move(675,575)
        self.startButton.clicked.connect(self.redirectScreen2)
    
    def home(self):

        self.pixmap = QPixmap('images/htimg1.jpg')
        self.label.setPixmap(self.pixmap)
        self.pixmap.scaled(256, 256)
        self.label1 = QtWidgets.QLabel(self)
        self.label1.move(535,50)
        self.label1.setFixedSize(370,470)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setText("Nisandigdhak: Word Sense Disambiguation Framework for the Marathi Language \n\n Word Sense Disambiguation (WSD) is one of the most challenging problems in the research area of natural language processing. To find the correct sense of the word in a particular context is referred to as Word Sense Disambiguation.\n\n  WSD serves as an intermediate step for consideration in almost every Natural language application such as Machine Translation (MT), Information Retrieval (IR), Information Extraction, Question Answering System, Sentiment Analysis, Named Entity Recognition, Text Mining, Speech Processing, and Text processing, etc.\n\n  In the Marathi language, words have several distinct senses. Word are grouped into different word classes called ‘Part of Speech’. As nouns are predominantly occurring ambiguous entity in the Marathi sentence. The focus of the Nisandigdhak framework is majorly around nouns compare to other parts of speech categories of the Marathi language.\n\n  This framework is worked on only the Health domain, Tourism domain, and News domain respectively. This is the first attempt at developing the Marathi language WSD framework for Nouns.")
        self.label1.setWordWrap(True)
        self.label1.show()
        self.updateLabelSize()
    
    def help(self):
        self.label1.close()
        self.label.setText("Help")
        self.updateLabelSize()
        #self.label1.close()
    
    def about(self):
        #self.label.setText("About")
        self.label1.close()
        self.label.setText("  This framework is meant to build for disambiguating the Marathi language Noun part of speech only.\n\n  This framework is copyright reserved.\n\n  Email Support : Submit email support query to patilamit03@gmail.com\n\n \nUnder the guidance by:\n\n  Centre for Development of Advanced Computing (C-DAC), Pune\n\n  School of Computer Science, KBC North Maharashtra University, Jalgaon")
        self.label.resize(300,40)
        self.label.setWordWrap(True)
        self.updateLabelSize()
        #self.label1.close()
    
    def updateLabelSize(self):
        self.label.adjustSize()
    
    def redirectScreen2(self):
        self.screen2 = screen2.Screen2()
        self.screen2.show()
        self.close()

if __name__=='__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())