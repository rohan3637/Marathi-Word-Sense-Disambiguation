from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore 
import sys

import screen4
import screen3
import main


metrics = {
    "Health":{
        'precision': 0.8720906168027753,
        'recall': 0.8991474651522301,
        'f1_score': 0.8822811491208558
    },
    "Tourism":{
        'precision': 0.8497603247872639,
        'recall': 0.8551639023439204,
        'f1_score': 0.8514397356618174
    },
    "News":{
        'f1_score': 0.6471299134555717,
        'precision': 0.7756143988284564,
        'recall': 0.6103175607805659
    }  
}

black_text = "<span style=\" font-size:15px; font-weight:600; color:black;\" >{}</span> "


class CustomLabel(QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLabel.mousePressEvent(self, event)


class Screen5(QMainWindow):
    def __init__(self, textEditText, screen3_content = None):
        super(Screen5, self).__init__()
        self.setWindowTitle("NISANDIGDHAK")
        self.setFixedSize(950,500)
        self.textEditText = textEditText
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

        self.current = 5
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
        
        METRIC_LABEL_X, METRIC_LABEL_Y = 250, 220


        self.stepLabel[1].clicked.connect(self.anyPageRedirect1)
        self.stepLabel[2].clicked.connect(self.anyPageRedirect2)
        self.stepLabel[3].clicked.connect(self.anyPageRedirect3)
        self.stepLabel[4].clicked.connect(self.anyPageRedirect4)
        self.stepLabel[5].clicked.connect(self.anyPageRedirect5)

        self.precisionLabel = QLabel(self)
        self.precisionLabel.setText("Precision")
        self.precisionLabel.move(METRIC_LABEL_X, METRIC_LABEL_Y)
        self.precisionLabel.setFixedSize(100,20)
        self.precisionLabel.setStyleSheet("""
            font-weight:bold;
            font-size: 15px;
        """)


        self.precisionTextEdit = QTextEdit(self)
        self.precisionTextEdit.move(METRIC_LABEL_X-25, METRIC_LABEL_Y+30)
        self.precisionTextEdit.setFixedSize(100,30)
        precision = str(metrics[self.screen3_content["domain"]]["precision"])[:4]
        self.precisionTextEdit.setText(black_text.format(precision))


        self.recallLabel = QLabel(self)
        self.recallLabel.setText("Recall")
        self.recallLabel.move(METRIC_LABEL_X+200, METRIC_LABEL_Y)
        self.recallLabel.setFixedSize(100,20)
        self.recallLabel.setStyleSheet("""
            font-weight:bold;
            font-size: 15px;
        """)


        self.recallTextEdit = QTextEdit(self)
        self.recallTextEdit.move(METRIC_LABEL_X+200-25, METRIC_LABEL_Y+30)
        self.recallTextEdit.setFixedSize(100,30)
        recall = str(metrics[self.screen3_content["domain"]]["recall"])[:4]
        self.recallTextEdit.setText(black_text.format(recall))



        self.fscoreLabel = QLabel(self)
        self.fscoreLabel.setText("F-Measure")
        self.fscoreLabel.move(METRIC_LABEL_X+400, METRIC_LABEL_Y)
        self.fscoreLabel.setFixedSize(100,20)
        self.fscoreLabel.setStyleSheet("""
            font-weight:bold;
            font-size: 15px;
        """)

        self.fscoreTextEdit = QTextEdit(self)
        self.fscoreTextEdit.move(METRIC_LABEL_X + 400-10, METRIC_LABEL_Y+30)
        self.fscoreTextEdit.setFixedSize(100,30)
        fscore = str(metrics[self.screen3_content["domain"]]["f1_score"])[:4]
        self.fscoreTextEdit.setText(black_text.format(fscore))



        self.backButton = QPushButton(self)
        self.backButton.setText("Back")
        self.backButton.move(325, 350)
        self.backButton.setFixedSize(100, 40)
        self.backButton.clicked.connect(self.backBtnPress)


        self.exitButton = QPushButton(self)
        self.exitButton.setText("Exit")
        self.exitButton.move(500, 350)
        self.exitButton.setFixedSize(100, 40)
        self.exitButton.clicked.connect(self.closeDialog)
    
    def backBtnPress(self):
        self.screen4 = screen4.Screen4(self.textEditText, screen3_content=self.screen3_content)
        self.screen4.disambiguateTextEdit.setText(self.textEditText)
        self.screen4.show()
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
        print("Pressed")
        if 4 < self.current:
            self.screen4 = screen4.Screen4(self.screen3_content["nouns"], self.screen3_content)
            self.screen4.disambiguateTextEdit.setText(self.textEditText)
            self.screen4.show()
            self.close()
    
    def anyPageRedirect5(self):
        print("Pressed")
        if 5 < self.current:
            print(5)



# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     win = Screen5()
#     win.show()
#     sys.exit(app.exec_())