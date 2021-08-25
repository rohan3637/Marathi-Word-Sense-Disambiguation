from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui
import sys

import screen5
import screen3
import main
import screen2


class CustomLabel(QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLabel.mousePressEvent(self, event)

class Screen4(QMainWindow):
    def __init__(self, nouns, screen3_content = None):
        super(Screen4, self).__init__()
        self.setWindowTitle("NISANDIGDHAK")
        self.setFixedSize(950,500)
        self.nouns = nouns
        self.screen3_content = screen3_content
        self.initUI()
    
    def initUI(self):

        self.homeButton = QtWidgets.QPushButton(self)
        self.homeButton.setText("Home")
        self.homeButton.move(0,0)
        self.homeButton.clicked.connect(self.homeBtnRedirect)

        self.helpButton = QtWidgets.QPushButton(self)
        self.helpButton.setText("Help")
        self.helpButton.move(100,0)

        self.aboutButton = QtWidgets.QPushButton(self)
        self.aboutButton.setText("About")
        self.aboutButton.move(200,0)
        self.aboutButton.clicked.connect(self.aboutBtnRedirect)

        self.current = 4
        LABEL_X, LABEL_Y = 150,100
        LINE_X, LINE_Y = 200,122
        STEP_X, STEP_Y = 150, 155


        self.stepLabel = [0] * 6



        for i in range(1,6):
            if i == self.current:
                self.stepLabel[i] = CustomLabel(self)
                self.stepLabel[i].setText(str(i))
                self.stepLabel[i].move(LABEL_X, LABEL_Y)
                self.stepLabel[i].setFixedSize(50,50)
                self.stepLabel[i].setStyleSheet("""
                    border:3px solid #4285F4;
                    border-radius: 25px;
                    font-weight: bold;
                    font-size:20px;
                    background-color:#4285F4;
                    color:white;
                """)
                self.stepLabel[i].setAlignment(QtCore.Qt.AlignCenter)

                self.stepNameLabel = QLabel(self)
                self.stepNameLabel.setText(f"STEP {i}")
                self.stepNameLabel.move(STEP_X, STEP_Y)
                self.stepNameLabel.setFixedSize(75,25)
                self.stepNameLabel.setStyleSheet("""
                    font-weight:bold;
                    font-size:15px;
                    color:#4285F4;
                """)

                if i+1 <= 5:
                    self.line = QLabel(self)
                    self.line.move(LINE_X, LINE_Y)
                    self.line.setFixedSize(100, 5)
                    self.line.setStyleSheet("""
                        background-color: grey;
                    """)

            if i < self.current:
                self.stepLabel[i] = CustomLabel(self)
                self.stepLabel[i].setText(str(i))
                self.stepLabel[i].move(LABEL_X, LABEL_Y)
                self.stepLabel[i].setFixedSize(50,50)
                self.stepLabel[i].setStyleSheet("""
                    border:3px solid green;
                    border-radius: 25px;
                    font-weight: bold;
                    font-size:20px;
                    color:green;
                """)
                self.stepLabel[i].setAlignment(QtCore.Qt.AlignCenter)

                self.stepNameLabel = QLabel(self)
                self.stepNameLabel.setText(f"STEP {i}")
                self.stepNameLabel.move(STEP_X, STEP_Y)
                self.stepNameLabel.setFixedSize(75,25)
                self.stepNameLabel.setStyleSheet("""
                    font-weight:bold;
                    font-size:15px;
                    color:green;
                """)

                if i+1 == self.current:
                    self.line = QLabel(self)
                    self.line.move(LINE_X, LINE_Y)
                    self.line.setFixedSize(100, 5)
                    self.line.setStyleSheet("""
                        background-color: #4285F4;
                    """)
                else:
                    self.line = QLabel(self)
                    self.line.move(LINE_X, LINE_Y)
                    self.line.setFixedSize(100, 5)
                    self.line.setStyleSheet("""
                        background-color: green;
                    """)
            
            if i>self.current:
                self.stepLabel[i] = CustomLabel(self)
                self.stepLabel[i].setText(str(i))
                self.stepLabel[i].move(LABEL_X, LABEL_Y)
                self.stepLabel[i].setFixedSize(50,50)
                self.stepLabel[i].setStyleSheet("""
                    border:3px solid grey;
                    border-radius: 25px;
                    font-weight: bold;
                    font-size:20px;
                    color:grey;
                """)
                self.stepLabel[i].setAlignment(QtCore.Qt.AlignCenter)

                self.stepNameLabel = QLabel(self)
                self.stepNameLabel.setText(f"STEP {i}")
                self.stepNameLabel.move(STEP_X, STEP_Y)
                self.stepNameLabel.setFixedSize(75,25)
                self.stepNameLabel.setStyleSheet("""
                    font-weight:bold;
                    font-size:15px;
                    color:grey;
                """)

                if i+1 <= 5:
                    self.line = QLabel(self)
                    self.line.move(LINE_X, LINE_Y)
                    self.line.setFixedSize(100, 5)
                    self.line.setStyleSheet("""
                        background-color: grey;
                    """)
            
            LABEL_X +=150
            LINE_X +=150
            STEP_X +=150


        self.stepLabel[1].clicked.connect(self.anyPageRedirect1)
        self.stepLabel[2].clicked.connect(self.anyPageRedirect2)
        self.stepLabel[3].clicked.connect(self.anyPageRedirect3)
        self.stepLabel[4].clicked.connect(self.anyPageRedirect4)
        self.stepLabel[5].clicked.connect(self.anyPageRedirect5)

        
        
        self.disambiguateInputLabel = QLabel(self)
        self.disambiguateInputLabel.setText("DISAMBIGUATE NOUNS")
        self.disambiguateInputLabel.move(150,225)
        self.disambiguateInputLabel.setFixedSize(225, 25)
        self.disambiguateInputLabel.setStyleSheet("""
            font-weight:bold;
            font-size:15px;
        """)
        self.disambiguateInputLabel.setAlignment(QtCore.Qt.AlignLeft)

        self.disambiguateTextEdit = QTextEdit(self)
        # self.disambiguateTextEdit.setText("This is example text.")
        self.disambiguateTextEdit.move(150,255)
        self.disambiguateTextEdit.setFixedSize(650, 150)
        
        BUTTON_X, BUTTON_Y = 150, 430

        self.saveButton = QPushButton(self)
        self.saveButton.setText("Save Result")
        self.saveButton.move(BUTTON_X,BUTTON_Y)
        self.saveButton.setFixedSize(150,25)
        self.saveButton.setStyleSheet("""
            font-weight:bold;
        """)
        self.saveButton.clicked.connect(self.saveBtnAction)

        self.accuracyButton = QPushButton(self)
        self.accuracyButton.setText("View Accuracy")
        self.accuracyButton.move(BUTTON_X+250,BUTTON_Y)
        self.accuracyButton.setFixedSize(150,25)
        self.accuracyButton.setStyleSheet("""
            font-weight:bold;
        """)
        self.accuracyButton.clicked.connect(self.redirectScreen5)

        self.exitButton = QPushButton(self)
        self.exitButton.setText("Exit")
        self.exitButton.move(BUTTON_X+500,BUTTON_Y)
        self.exitButton.setFixedSize(150,25)
        self.exitButton.setStyleSheet("""
            font-weight:bold;
        """)
        self.exitButton.clicked.connect(self.closeDialog)
    



    def anyPageRedirect1(self):
        self.main = main.MainWindow()
        self.main.show()
        self.close()
    
    def anyPageRedirect2(self):
        import screen2

        self.screen2 = screen2.Screen2()
        self.screen2.paragraphTextEdit.setText("")

        sent = self.screen3_content["sentence"]
        words = sent.split(" ")
        x = []
        for word in words:
            if word!="" and word!=" ":
                x.append(word)
        
        sent = " ".join(x)

        self.screen2.paragraphTextEdit.setText(self.screen3_content["screen2Text"])
        self.screen2.show()
        self.close()

    def anyPageRedirect3(self):
        self.screen3 = screen3.Screen3(self.screen3_content["sentence"], self.screen3_content["nouns"], self.screen3_content["domain"], self.screen3_content["screen2Text"], self.screen3_content["screen3_noun_dicts"])
        self.screen3.wordSenseTextEdit.setText("")
        self.screen3.posTaggingTextEdit.setText("")
        self.screen3.wordSenseTextEdit.setHtml(self.screen3_content["word_sense_text_edit"])
        self.screen3.posTaggingTextEdit.setHtml(self.screen3_content["pos_tagging_text_edit"])
        self.screen3.show()
        self.close()
    
    def anyPageRedirect4(self):
        if 4 < self.current:
            print(4)
    
    def anyPageRedirect5(self):
        if 5 < self.current:
            print(5)





    def redirectScreen5(self):
        self.screen5 = screen5.Screen5(self.disambiguateTextEdit.toHtml(), self.screen3_content)
        self.screen5.show()
        self.close()
    
    def closeDialog(self):

        quit_msg = "Are you sure you want to exit the Application?"
        messageBox = QtWidgets.QMessageBox()
        reply = messageBox.question(self, 'Message', 
                        quit_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            self.close()
        else:
            messageBox.done(1)
        
    
    def homeBtnRedirect(self):
        self.mainWindow = main.MainWindow()
        self.mainWindow.home()
        self.mainWindow.show()
        self.close()
    
    def aboutBtnRedirect(self):
        self.mainWindow = main.MainWindow()
        self.mainWindow.about()
        self.mainWindow.show()
        self.close()

    def saveBtnAction(self):

        quit_msg = "Are you sure you want to save?"
        messageBox = QtWidgets.QMessageBox()
        reply = messageBox.question(self, 'Message', 
                        quit_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            content = self.disambiguateTextEdit.toPlainText()
            fil = open("disambiguate_text.txt", "w", encoding="utf-8")
            fil.write(content)
            messageBox.done(1)
        else:
            messageBox.done(1)





# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     win = Screen4()
#     win.show()
#     sys.exit(app.exec_())