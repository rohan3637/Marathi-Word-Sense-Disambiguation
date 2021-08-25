from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui
import sys
import main

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import stemmer

import numpy as np

import screen3
import main

from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

health_word_index = pickle.load(open("Health_Model/h0word_index.pkl", "rb"))
health_pos_index = pickle.load(open("Health_Model/h0pos_index.pkl", "rb"))

tourism_word_index = pickle.load(open("Tourism_Model/t0word_index.pkl", "rb"))
tourism_pos_index = pickle.load(open("Tourism_Model/t0pos_index.pkl", "rb"))

news_word_index = pickle.load(open("News_Model/news_word_index.pkl", "rb"))
news_pos_index = pickle.load(open("News_Model/news_tag_index.pkl", "rb"))

nouns = pickle.load(open("WordSenseDisambiguationModel/nouns.pkl", "rb"))
cleaned_noun_data = pickle.load(open("WordSenseDisambiguationModel/cleaned_noun_data.pkl", "rb"))
meanings = pickle.load(open("WordSenseDisambiguationModel/meanings.pkl", "rb"))


tourism_word_mapping = pickle.load(open("tourism_word_mapping.pkl","rb"))
health_word_mapping = pickle.load(open("health_word_mapping.pkl","rb"))

health_pos = {}
for key, value in health_pos_index.items():
    print(key)
    print(value)
    health_pos[value] = key

tourism_pos = {}
for key, value in tourism_pos_index.items():
    tourism_pos[value] = key

news_pos = {}
for key, value in news_pos_index.items():
    news_pos[value] = key


def preprocess_tourism_input_text(text, MAXLEN=113,word_index=tourism_word_index):
    sentence = text.split(" ")
    for i in range(len(sentence)):
      if sentence[i]=="\n" or sentence[i]=="  ":
        sentence[i]=" ";
    sentence_numeric = []
    for word in sentence:
        try:
            sentence_numeric.append(word_index[word])
        except:
            sentence_numeric.append(word_index["_OOV_"])
    sentence_numeric = pad_sequences([sentence_numeric], maxlen=MAXLEN, padding="pre",truncating="post")
    return sentence_numeric.reshape((1,113))

def preprocess_health_input_text(text, MAXLEN=100,word_index=health_word_index):
    sentence = text.split(" ");
    for i in range(len(sentence)):
      if sentence[i]=="\n" or sentence[i]=="  ":
        sentence[i]=" "
    sentence_numeric = []
    for word in sentence:
        try:
            sentence_numeric.append(word_index[word])
        except:
            sentence_numeric.append(word_index["_OOV_"])
    sentence_numeric = pad_sequences([sentence_numeric], maxlen=MAXLEN, padding="pre",truncating="post")
    return sentence_numeric.reshape((1,100))


def preprocess_news_input_text(text, MAXLEN=129,word_index=news_word_index):
    sentence = text.split(" ")
    for i in range(len(sentence)):
      if sentence[i]=="\n" or sentence[i]=="  ":
        sentence[i]=" ";
    sentence_numeric = []
    for word in sentence:
        try:
            sentence_numeric.append(word_index[word])
        except:
            sentence_numeric.append(word_index["OOV"])
    sentence_numeric = pad_sequences([sentence_numeric], maxlen=MAXLEN, padding="pre",truncating="post")
    return sentence_numeric.reshape((1,MAXLEN))



def getPredictions(predictions):
    pred = []
    for i in predictions[0]:
        pred.append(np.argmax(i))
    return pred


health_json_file = open('Health_Model/h0model.json', 'r')
health_loaded_model_json = health_json_file.read()
health_json_file.close()
health_model = model_from_json(health_loaded_model_json)
health_model.load_weights("Health_Model/h0model.h5")

tourism_json_file = open('Tourism_Model/t0model.json', 'r')
tourism_loaded_model_json = tourism_json_file.read()
tourism_json_file.close()
tourism_model = model_from_json(tourism_loaded_model_json)
tourism_model.load_weights("Tourism_Model/t0model.h5")

news_json_file = open('News_Model/news_model.json', 'r')
news_loaded_model_json = news_json_file.read()
news_json_file.close()
news_model = model_from_json(news_loaded_model_json)
news_model.load_weights("News_Model/news_model_weights.h5")


red_text = "<span style=\" font-size:15px; font-weight:600; color:violet;\" >{}</span> "
green_text = "<span style=\" font-size:15px; font-weight:600; color:green;\" >{}</span> "
yellow_text = "<span style=\" font-size:15px; font-weight:600; color:yellow;\" >{}</span> "
blue_text = "<span style=\" font-size:15px; font-weight:600; color:blue;\" >{}</span> "
black_text = "<span style=\" font-size:15px; font-weight:600; color:black;\" >{}</span> "

pos_tag_color_text = {
    'n':red_text,
    'r':green_text,
    'a':yellow_text,
    'v':blue_text,
    'u':black_text,
    "_PAD_":black_text
}


class CustomLabel(QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLabel.mousePressEvent(self, event)


class Screen2(QMainWindow):
    def __init__(self, screen2_content = None):
        super(Screen2, self).__init__()
        self.setWindowTitle("NISANDIGDHAK")
        self.screen2Content = screen2_content
        self.setFixedSize(950,700)
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



        self.current = 2
        LABEL_X, LABEL_Y = 150,100
        LINE_X, LINE_Y = 200,122
        STEP_X, STEP_Y = 150, 155

        self.stepLabel = [0]*6

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


        self.domainLabel = QLabel(self)
        self.domainLabel.setText("Choose Domain")
        self.domainLabel.move(400, 275)
        self.domainLabel.setFixedSize(150,25)
        self.domainLabel.setStyleSheet("""
            font-weight:bold;
        """)
        self.domainLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.domainComboBox = QComboBox(self)
        self.domainComboBox.setGeometry(400, 300, 150, 30)
        domainList = ["Tourism", "Health"]
        self.domainComboBox.addItems(domainList)

        self.enterParaLabel = QLabel(self)
        self.enterParaLabel.setText("Enter Paragraph\n (Max. 100 Words)")
        self.enterParaLabel.move(100, 450)
        self.enterParaLabel.setFixedSize(125, 35)
        self.enterParaLabel.setStyleSheet("""
            font-weight:bold;
        """)
        self.enterParaLabel.setAlignment(QtCore.Qt.AlignJustify)

        self.paragraphTextEdit = QTextEdit(self)
        self.paragraphTextEdit.move(235, 350)
        self.paragraphTextEdit.setFixedSize(500, 250)

        
        self.disambiguateButton = QPushButton(self)
        self.disambiguateButton.move(375, 625)
        self.disambiguateButton.setText("Disambiguate Word Sense")
        self.disambiguateButton.setStyleSheet("""
            font-weight:bold;
        """)
        self.disambiguateButton.setFixedSize(200,30)
        self.disambiguateButton.clicked.connect(self.redirectScreen3)

        self.uploadFileLabel = QLabel(self)
        self.uploadFileLabel.setText("Upload Text File")
        self.uploadFileLabel.move(765, 400)
        self.uploadFileLabel.setFixedSize(150,25)
        self.uploadFileLabel.setStyleSheet("""
            font-weight:bold;
        """)
        self.uploadFileLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.uploadFileButton = QPushButton(self)
        self.uploadFileButton.setText("Browse")
        self.uploadFileButton.setStyleSheet("""
            font-weight:bold;
        """)
        self.uploadFileButton.move(765, 435)
        self.uploadFileButton.setFixedSize(150,25)
        self.uploadFileButton.clicked.connect(self.browseFile)

        self.clearTextButton = QPushButton(self)
        self.clearTextButton.setText("Clear Text")
        self.clearTextButton.setStyleSheet("""
            font-weight:bold;
        """)
        self.clearTextButton.move(765, 475)
        self.clearTextButton.setFixedSize(150,25)
        self.clearTextButton.clicked.connect(self.clearText)


    def browseFile(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(self, "Upload Text", filter="*.txt")
            opened_file = open(file_path, "r", encoding="utf-8")
            file_content = opened_file.read()
            self.paragraphTextEdit.setText(file_content)
        except:
            pass

    def clearText(self):
        self.paragraphTextEdit.setText("")
    
    def redirectScreen3(self):
        content = self.paragraphTextEdit.toPlainText().replace("."," .")
        current_combo_text = self.domainComboBox.currentText()

        num_words = len(content.split(" "))

        if num_words > 100:
            self.wordsAlertMessage()
        
        else:
            self.helperRedirect()

    
    def anyPageRedirect1(self):
        self.main = main.MainWindow()
        self.main.show()
        self.close()
    
    def anyPageRedirect2(self):
        print(2)

    def anyPageRedirect3(self):
        print("Pressed")
        if 3 < self.current:
            print(3)
    
    def anyPageRedirect4(self):
        print("Pressed")
        if 4 < self.current:
            print(4)
    
    def anyPageRedirect5(self):
        print("Pressed")
        if 5 < self.current:
            print(5)


    def helperRedirect(self):
        content = self.paragraphTextEdit.toPlainText().replace("."," .")
        current_combo_text = self.domainComboBox.currentText()

        content = ' '.join(content.split(" ")[:100])
        # print(len(content.split(" ")))

        self.domain = current_combo_text


        all_nouns = []

        if len(content) != 0:
            if current_combo_text == "Health":
                # print("====> Health")
                predictions = getPredictions((health_model.predict(preprocess_health_input_text(content))))
                print(predictions)
                preds = [i for i in predictions if i != 0]
                print(preds)
                pos = []
                for i in preds:
                    pos.append(health_pos[i])
                word_with_pos = {}
                print(content)
                text = content.split(" ")
                print(text)
                for i in range(len(text)):
                    word_with_pos[text[i]] = pos[i]
                output = ""
                for key, value in word_with_pos.items():
                    insert_value = key #+ " " + value
                    output = output + pos_tag_color_text[value].format(insert_value)
                    #print(output)
                    if value == "n":
                        all_nouns.append(key)

            elif current_combo_text == "Tourism":
                # print("====> Tourism")
                predictions = getPredictions((tourism_model.predict(preprocess_tourism_input_text(content))))
                preds = [i for i in predictions if i != 0]
                pos = []
                for i in preds:
                    pos.append(tourism_pos[i])
                word_with_pos = {}
                text = content.split(" ")
                for i in range(len(text)):
                    word_with_pos[text[i]] = pos[i]
                output = ""
                for key, value in word_with_pos.items():
                    insert_value = key #+ " " + value
                    output = output + pos_tag_color_text[value].format(insert_value)
                    print(output)
                    if value == "n":
                        all_nouns.append(key)
                       
            elif current_combo_text == "News":
                # print("====> News")
                predictions = getPredictions((news_model.predict(preprocess_news_input_text(content))))
                preds = [i for i in predictions if i != 0]
                pos = []
                for i in preds:
                    pos.append(news_pos[i])
                word_with_pos = {}
                text = content.split(" ")
                for i in range(len(text)):
                    word_with_pos[text[i]] = pos[i]
                output = ""
                for key, value in word_with_pos.items():
                    insert_value = key
                    output = output + pos_tag_color_text[value].format(insert_value)
                    if value == "n":
                        all_nouns.append(key)
        
            wordsense_output = ""
            screen3_nouns = []
            screen3_noun_dicts = []

            for noun in all_nouns:
                senses, noun_dict = self.getSense(noun)
                screen3_noun_dicts.append(noun_dict)

                if senses:

                    wordsense_output = wordsense_output + red_text.format(str(noun)) + ":" + "<br>"

                    index = 1
                    for sense in senses:
                        wordsense_output = wordsense_output + str(black_text.format(index)) + ". "  + str(black_text.format(sense)) + "<br>"
                        index+=1

                    screen3_nouns.append(noun)
            
            self.screen3 = screen3.Screen3(content, screen3_nouns, self.domain, self.paragraphTextEdit.toPlainText(), screen3_noun_dicts)
            self.screen3.posTaggingTextEdit.setText(output)


            self.screen3.wordSenseTextEdit.setText(wordsense_output)
            self.screen3.show()
            self.close()
        else:
            self.alertDialog()


    def consine_similarity(self, l1, l2, rvector):
        c = 0
        for i in range(len(rvector)): 
            c+= l1[i]*l2[i] 
        cosine = c / float((sum(l1)*sum(l2))**0.5)
        return cosine


    def getSense(self, noun):
        syn_ids = []
        noun_dict = {noun:[noun]}
        try:
            if noun in nouns:
                syn_ids += nouns[noun]
            
            elif self.domainComboBox.currentText() == "Tourism":
                if noun in tourism_word_mapping:
                    for temp in tourism_word_mapping[noun]:
                        if temp in nouns:
                            noun_dict[noun].append(temp)
                            syn_ids += nouns[temp]
            
            elif self.domainComboBox.currentText() == "Health":
                if noun in health_word_mapping:
                    for temp in health_word_mapping[noun]:
                        if temp in nouns:
                            noun_dict[noun].append(temp)
                            syn_ids += nouns[temp]
            # else:
            #     stemmed_noun = stemmer.stemWord(noun)
            #     # print(stemmed_noun)
            #     syn_ids += nouns[stemmed_noun]

            all_senses = []


            for i in range(len(syn_ids)):

                
                if ":" in meanings[syn_ids[i]]:
                    all_senses.append(meanings[syn_ids[i]].split(":")[0])
                else:
                    all_senses.append(meanings[syn_ids[i]].split(".")[0])

            return all_senses, noun_dict

        except:
            return None, {}                


    def wordsAlertMessage(self):
        alert_message = "Only 100 words will be considered for Word Sense Disambiguation"
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QMessageBox.Information)
        messageBox.setText(alert_message)
        messageBox.setWindowTitle("Alert Message")
        messageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        messageBox.buttonClicked.connect(self.msgbtn)

        ret_val = messageBox.exec_()
    

    def msgbtn(self, i):
        ans = i.text()
        if ans == "OK":
            self.helperRedirect()
        else:
            pass


    def alertDialog(self):
        quit_msg = "Please Enter some Text"
        messageBox = QtWidgets.QMessageBox()
        reply = messageBox.question(self, 'Message', 
                        quit_msg, QtWidgets.QMessageBox.Ok)

        if reply == QtWidgets.QMessageBox.Ok:
            messageBox.done(1)
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



# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     win = Screen2()
#     win.show()
#     sys.exit(app.exec_())
