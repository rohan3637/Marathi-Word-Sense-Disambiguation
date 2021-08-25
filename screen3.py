from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore 
import sys
import numpy as np

import screen4
import main
import pickle
import math
from gensim.models import Word2Vec


noun_vectors = pickle.load(open("WordSenseDisambiguationModel/new_models/noun_vectors.pkl", "rb"))
word2vec_model = Word2Vec.load("WordSenseDisambiguationModel/new_models/word2vec_model.model")

nouns = pickle.load(open("WordSenseDisambiguationModel/nouns.pkl", "rb"))
cleaned_noun_data = pickle.load(open("WordSenseDisambiguationModel/cleaned_noun_data.pkl", "rb"))
meanings = pickle.load(open("WordSenseDisambiguationModel/meanings.pkl", "rb"))


red_text = "<span style=\" font-size:15px; font-weight:600; color:violet;\" >{}</span> "
green_text = "<span style=\" font-size:15px; font-weight:600; color:green;\" >{}</span> "
yellow_text = "<span style=\" font-size:15px; font-weight:600; color:yellow;\" >{}</span> "
blue_text = "<span style=\" font-size:15px; font-weight:600; color:blue;\" >{}</span> "
black_text = "<span style=\" font-size:15px; font-weight:600; color:black;\" >{}</span> "


class CustomLabel(QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLabel.mousePressEvent(self, event)


class Screen3(QMainWindow):
    def __init__(self, sentence, nouns, domain, screen2Text, screen3_noun_dicts = None):
        super(Screen3, self).__init__()
        self.setWindowTitle("NISANDIGDHAK")
        self.setFixedSize(950,750)
        self.nouns = nouns
        self.domain = domain
        self.screen3_noun_dicts = screen3_noun_dicts
        self.sentence = sentence.strip()
        print(f"Sentence : {self.sentence}")
        self.screen2Text = screen2Text
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

        self.current = 3
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

        
        self.posTaggingInputLabel = QLabel(self)
        self.posTaggingInputLabel.setText("POS TAGGING OF INPUT TEXT")
        self.posTaggingInputLabel.move(150,225)
        self.posTaggingInputLabel.setFixedSize(225, 25)
        self.posTaggingInputLabel.setStyleSheet("""
            font-weight:bold;
            font-size:15px;
        """)
        self.posTaggingInputLabel.setAlignment(QtCore.Qt.AlignLeft)

        self.posTaggingTextEdit = QTextEdit(self)
        self.posTaggingTextEdit.move(150,255)
        self.posTaggingTextEdit.setFixedSize(650, 150)

        self.nounColor = QLabel(self)
        self.nounColor.move(300, 410)
        self.nounColor.setFixedSize(25,25)
        self.nounColor.setStyleSheet("""
            background-color:violet;
        """)

        self.nounLabel = QLabel(self)
        self.nounLabel.setText("NOUN")
        self.nounLabel.move(330, 407)

        self.verbColor = QLabel(self)
        self.verbColor.move(400, 410)
        self.verbColor.setFixedSize(25,25)
        self.verbColor.setStyleSheet("""
            background-color:blue;
        """)

        self.verbLabel = QLabel(self)
        self.verbLabel.setText("VERB")
        self.verbLabel.move(430, 407)

        self.adverbColor = QLabel(self)
        self.adverbColor.move(500, 410)
        self.adverbColor.setFixedSize(25,25)
        self.adverbColor.setStyleSheet("""
            background-color:green;
        """)

        self.adverbLabel = QLabel(self)
        self.adverbLabel.setText("ADVERB")
        self.adverbLabel.move(530, 407)

        self.adjectiveColor = QLabel(self)
        self.adjectiveColor.move(600, 410)
        self.adjectiveColor.setFixedSize(25,25)
        self.adjectiveColor.setStyleSheet("""
            background-color:yellow;
        """)

        self.adjectiveLabel = QLabel(self)
        self.adjectiveLabel.setText("ADJECTIVE")
        self.adjectiveLabel.move(630, 407)

        self.label = QLabel(self)
        self.label.setText("Nouns Heighlighted in Violet Color")
        self.label.move(400, 440)
        self.label.setFixedSize(200,20)


        self.wordSenseInputLabel = QLabel(self)
        self.wordSenseInputLabel.setText("WORD SENSES FOR NOUNS")
        self.wordSenseInputLabel.move(150,465)
        self.wordSenseInputLabel.setFixedSize(225, 25)
        self.wordSenseInputLabel.setStyleSheet("""
            font-weight:bold;
            font-size:15px;
        """)
        self.wordSenseInputLabel.setAlignment(QtCore.Qt.AlignLeft)

        self.wordSenseTextEdit = QTextEdit(self)
        self.wordSenseTextEdit.move(150,495)
        self.wordSenseTextEdit.setFixedSize(650, 150)

        self.correctWordSenseButton = QPushButton(self)
        self.correctWordSenseButton.setText("Correct Wordsense")
        self.correctWordSenseButton.move(350, 650)
        self.correctWordSenseButton.setFixedSize(225,30)
        self.correctWordSenseButton.setStyleSheet("""
            font-weight:bold;
        """)
        self.correctWordSenseButton.clicked.connect(self.redirectScreen4)


    def anyPageRedirect1(self):
        self.main = main.MainWindow()
        self.main.show()
        self.close()
    
    def anyPageRedirect2(self):
        import screen2

        self.screen2 = screen2.Screen2()
        self.screen2.paragraphTextEdit.setText("")
        sent = self.sentence
        words = sent.split(" ")
        x = []
        for word in words:
            if word!="" and word!=" ":
                x.append(word)
        
        sent = " ".join(x)

        self.screen2.paragraphTextEdit.setText(self.screen2Text)
        self.screen2.show()
        self.close()

    def anyPageRedirect3(self):
        if 3 < self.current:
            print(3)
    
    def anyPageRedirect4(self):
        if 4 < self.current:
            print(4)
    
    def anyPageRedirect5(self):
        if 5 < self.current:
            print(5)
    

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
    
    
    def redirectScreen4(self):
        output = ""
        present_nouns = {}
        for noun in self.nouns:
            for n_dict in self.screen3_noun_dicts:
                if noun in n_dict:
                    for n in n_dict[noun]:
                        try:
                            z = noun_vectors[n]
                            present_nouns[noun] = n
                        except:
                            continue
        # print(self.screen3_noun_dicts)
        # print(len(self.nouns))
        # print(len(present_nouns))
        # print(self.nouns)
        # print(present_nouns)
        for noun in present_nouns:
            sense = self.getSense(self.sentence, noun, present_nouns[noun])
            if sense!= None:
                output = output + red_text.format(noun) + " : " + sense + "<br>"

        screen3_content = {
            "sentence":self.sentence,
            "nouns":self.nouns,
            "pos_tagging_text_edit":self.posTaggingTextEdit.toHtml(),
            "word_sense_text_edit":self.wordSenseTextEdit.toHtml(),
            "domain":self.domain,
            "screen3_noun_dicts":self.screen3_noun_dicts,
            "screen2Text":self.screen2Text
        }

        self.screen4 = screen4.Screen4(nouns, screen3_content=screen3_content)
        self.screen4.disambiguateTextEdit.setText(output)
        self.screen4.show()
        self.close()

    

    def cosine_similarity(self,v1,v2):
        print(v1)
        print(v2)
        sumxx, sumxy, sumyy = 0, 0, 0
        for i in range(len(v1)):
            x = v1[i]; y = v2[i]
            sumxx += x*x
            sumyy += y*y
            sumxy += x*y
        return sumxy/math.sqrt(sumxx*sumyy)

    def getSense(self, sentence, noun, present_noun, noun_position = 1, noun_vectors = noun_vectors):
        sentence = sentence.strip().replace(".", " .").split(" ")
        sense_vector = 0
        count = 0
        position = 1
        for word in sentence:

            try:
                if noun!=word:
                    sense_vector += word2vec_model[word]
                    count += 1
                else:
                    if position != noun_position:
                        sense_vector += word2vec_model[present_noun]
                        count += 1
                    position += 1
            except Exception as e: 
                print(e)
                pass

        
        if noun in noun_vectors:
            cosines = {}
            for nid in noun_vectors[noun]:
                c = []
                for vector in noun_vectors[noun][nid]:
                    c.append(self.cosine_similarity(vector, sense_vector))
                cosines[nid] = max(c)
            
            # print(cosines)
            try:
                final_id = max(cosines, key = cosines.get)

                if ":" in meanings[final_id]:
                    final_sense = meanings[final_id].split(":")[0]
                else:
                    final_sense = meanings[final_id].split(".")[0]
            except:
                return None
            return black_text.format(final_sense)
        
        elif present_noun in noun_vectors:
            cosines = {}
            for nid in noun_vectors[present_noun]:
                c = []
                for vector in noun_vectors[present_noun][nid]:
                    c.append(self.cosine_similarity(vector, sense_vector))
                cosines[nid] = max(c)
            
            # print(cosines)
            try:
                final_id = max(cosines, key = cosines.get)

                if ":" in meanings[final_id]:
                    final_sense = meanings[final_id].split(":")[0]
                else:
                    final_sense = meanings[final_id].split(".")[0]
            except:
                return None
            return black_text.format(final_sense)

        else:
            return None

    # def consine_similarity(self, l1, l2, rvector):
    #     c = 0
    #     for i in range(len(rvector)): 
    #         c+= l1[i]*l2[i] 
    #     cosine = c / float((sum(l1)*sum(l2))**0.5)
    #     return cosine    
    

    # def getSense(self, sentence, noun):
    #     syn_ids = []
    #     scores = []
    #     ids = []
    #     try:
    #         syn_ids += nouns[noun]

    #         x = sentence.split(" ")
    #         for syn_id in syn_ids:
    #             y = cleaned_noun_data[syn_id][0].split(" ")

    #             x_set = {word for word in x}
    #             y_set = {word for word in y}

    #             rvector = x_set.union(y_set)
    #             l1, l2 = [], []

    #             for w in rvector:
    #                 if w in x_set:
    #                     l1.append(1)
    #                 else:
    #                     l1.append(0)
                    
    #                 if w in y_set:
    #                     l2.append(1)
    #                 else:
    #                     l2.append(0)
                
    #             cosine_score = self.consine_similarity(l1, l2, rvector)
    #             scores.append(cosine_score)
    #             ids.append(syn_id)
            
    #         final_id = ids[np.argmax(scores)]

            
    #         if ":" in meanings[final_id]:
    #             final_sense = meanings[final_id].split(":")[0]
    #         else:
    #             final_sense = meanings[final_id].split(".")[0]
    #         return black_text.format(final_sense)

    #     except:
    #         return None
