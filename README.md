<div align="center"><h1>Marathi Word Sense Disambiguation</h1></div>

## Approach

1. All the sentences along with their Parts of Speech (POS) tags are seperated from the textual data from each Domain (Health, News, Tourism).

2. Converting the textual data to numerical data by assigning index to each word.

3. Training a Bi-Directional LSTM model to predict the POS tag for a word.

4. Seperating the nouns, verbs, adverbs and adjectives.

5. Loading the nouns data containing all the senses along with some example sentences.

6. Using cosine similarity to find the correct sense of the noun from the input sentence.

## Instructions to run the Application
1. Open the project folder and Install all the dependencies by running this command in command prompt:

```
pip install requirements.txt
```

2. After successfully installing all the dependencies, get the "WordSenseDisambiguationModel" folder from the drive, unzip it and put it in this current directory i.e. directory with main.py file and run the following command to start the application:

```
python main.py
```


## Questions and Answers

1. <b>Which technique use in embedding layer?</b><br/>
Keras Embedding Layer was used which is trained during the model training process.

2. <b>Which activation function used?</b><br/>
Softmax Activation Function was used to the predict the output classes. Softmax axtivation function preduces a probability value between 0 to 1 for each class. The class with highest probability is the predicted class.

3. <b>What is the size of input matrix?</b><br/>
The input matrix was different for each domain (Tourism, Health, News) model. <br>
The input shapes are of the form (Number of sentences, Length of the sentences)<br/>
Tourism Domain: (22940, 113)<br/>
Health Domain: (9948, 100)<br/>
News Domain: (765, 129)

4. <b>How many hidden layer in NN model?</b><br/>
The Neural Network (NN) Model has one hidden Bi-Directional LSTM layer. Bi-Directional LSTM was used beacause these layers perform well in preserving the past data.

5. <b>How many gated memory unit per layer?</b><br/>
The number of gated memory units used is as follows:<br/>
Tourism Domain: 512<br/>
Health Domain: 256<br/>
News Domain: 512


6. <b>Which optimization applied to update weights among the different layer?</b><br/>
Adam optimizer with learning rate of 0.001 was used to update the weights among different layers.


7. <b>How many epoch is used to Training the model?</b><br/>
The number of epochs used for training the models are:<br/>
Tourism Domain: 10 epochs<br/>
Health Domain: 15 epochs<br/>
News Domain: 60 epochs

8. <b>What is the batch size?</b><br/>
The batch size used for training the models are:<br/>
Tourism Domain: 128<br/>
Health Domain: 128<br/>
News Domain: 128


9. <b>Which loss function is used?</b><br/>
categorical crossentropy was used as loss function. It is well suited for classification tasks involving classification of multiple classes.


## Architectures
#### POS tagging model for Health Domain
<div align="center">
    <img src="images/Health_Model_Architecture.png">
</div>

#### POS tagging model for Tourism Domain
<div align="center">
    <img src="images\Tourism_Model_Architecture.png">
</div>

#### POS tagging model for News Domain
<div align="center">
    <img src="images/News_Model_Architecture.png">
</div>

## Flow Chart for POS Tagging
<div align="center"><img src = "images/POS_Tagging_Flow_Chart.png"></div>

## Flow Chart for Word Sense Disambiguation
<div align="center">
    <img src="images/FlowChart_for_Marathi_WSD.png">
</div>

<div align="center"><h1>Marathi Word Sense Disambiguation</h1></div>

## Approach

1. All the sentences along with their Parts of Speech (POS) tags are seperated from the textual data from each Domain (Health, News, Tourism).

2. Converting the textual data to numerical data by assigning index to each word.

3. Training a Bi-Directional LSTM model to predict the POS tag for a word.

4. Seperating the nouns, verbs, adverbs and adjectives.

5. Loading the nouns data containing all the senses along with some example sentences.

6. Using cosine similarity to find the correct sense of the noun from the input sentence.

## Pseudocode

<b>Input: </b>A paragraph belonging to Health, News or Tourism Domain <br/>
<b>Output: </b>Correct sense of the nouns based on the context of the paragraph <br/>
(1) Seperate all the sentences in the paragraph <br/>
(2) for each sentence in sentences<br/>
(3) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;converting the sentence to numerical data by assigning index to each work and also padding the sentences;<br/>
(4) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;using the trained POS tagging model to predict the parts of speech for each word in the sentence;<br/>
(5) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gets all the available senses for the predicted nouns;<br/>
(6) End for<br/>
(7) for each noun in predicted nouns<br/>
(8) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;calculates the context vector for the noun by adding all the context vectors of the neighbour words;<br/>
(9) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;predicts the correct sense of the noun based on the cosine similarity of the context vector of the noun and the context vectors of all the sentences;<br/>
(10) End for<br/>
(11) Return the correct senses of the predicted nouns

## POS Tagging Workflow
<center><img src="./images/POS_TAGGING_Flowchart.png" align="center"></center>

## Wordsense Disambiguation Workflow
<center><img src="./images/WSD_Flowchart.png" align="center"></center>

## Instructions to run the Application

1. Open the project folder and Install all the dependencies by running this command in command prompt:

```
pip install requirements.txt
```

2. After successfully installing all the dependencies, get the "WordSenseDisambiguationModel" folder from the drive, unzip it and put it in this current directory i.e. directory with main.py file and run the following command to start the application:

```
python main.py
```

## Questions and Answers

1. <b>Which technique use in embedding layer?</b><br/>
   Keras Embedding Layer was used which is trained during the model training process.

2. <b>Which activation function used?</b><br/>
   Softmax Activation Function was used to the predict the output classes. Softmax axtivation function preduces a probability value between 0 to 1 for each class. The class with highest probability is the predicted class.

3. <b>What is the size of input matrix?</b><br/>
   The input matrix was different for each domain (Tourism, Health, News) model. <br>
   The input shapes are of the form (Number of sentences, Length of the sentences)<br/>
   Tourism Domain: (22940, 113)<br/>
   Health Domain: (9948, 100)<br/>
   News Domain: (765, 129)

4. <b>How many hidden layer in NN model?</b><br/>
   The Neural Network (NN) Model has one hidden Bi-Directional LSTM layer. Bi-Directional LSTM was used beacause these layers perform well in preserving the past data.

5. <b>How many gated memory unit per layer?</b><br/>
   The number of gated memory units used is as follows:<br/>
   Tourism Domain: 512<br/>
   Health Domain: 256<br/>
   News Domain: 512

6. <b>Which optimization applied to update weights among the different layer?</b><br/>
   Adam optimizer with learning rate of 0.001 was used to update the weights among different layers.

7. <b>How many epoch is used to Training the model?</b><br/>
   The number of epochs used for training the models are:<br/>
   Tourism Domain: 10 epochs<br/>
   Health Domain: 15 epochs<br/>
   News Domain: 60 epochs

8. <b>What is the batch size?</b><br/>
   The batch size used for training the models are:<br/>
   Tourism Domain: 128<br/>
   Health Domain: 128<br/>
   News Domain: 128

9. <b>Which loss function is used?</b><br/>
   categorical crossentropy was used as loss function. It is well suited for classification tasks involving classification of multiple classes.

## Architectures

#### POS tagging model for Health Domain

<div align="center">
    <img src="https://user-images.githubusercontent.com/58647922/124362393-1b658880-dc52-11eb-93e1-ba59b9916b36.png">
</div>

#### POS tagging model for Tourism Domain

<div align="center">
    <img src="https://user-images.githubusercontent.com/58647922/124362411-346e3980-dc52-11eb-8c20-2d0dae3dc211.png">
</div>

#### POS tagging model for News Domain

<div align="center">
    <img src="images/News_Model_Architecture.png">
</div>

## Flow Chart for POS Tagging

<div align="center"><img src = "images/POS_Tagging_Flow_Chart.png"></div>

## Flow Chart for Word Sense Disambiguation

<div align="center">
    <img src="images/FlowChart_for_Marathi_WSD.png">
</div>

## Answers to question:

1. <b>we modified the model many times from starting to till date, but the precision, recall, and F-measure values never changed. Are these static values passed to the model ?</b><br>
   Precision, Recall, F1- score and accuracy changed.

2. <b>How cosine similarity works for finding the correct senses of nouns?</b><br>
   Cosine similarity measures the similarity between two vectors of an inner product space. It is measured by the cosine of the angle between two vectors and determines whether two vectors are pointing in roughly the same direction. Cosine similarity is a metric used to measure how similar the documents are irrespective of their size in text analysis

3. <b>How cosine similarity show correct sense by multi vectors senses, explain with one simple example (by the formula)?</b><br>

4. <b>Provide algorithm/Sudo-code for the model.</b><br>
   input embedding layer -> 4 bilstm layer with dropouts -> 2 fully connected dense layer with dropouts -> time distributed dense output layer

5. <b>Which activation function we used in the model and why?</b><br>
   We used softmax activation. The softmax function is used as the activation function in the output layer of neural network models that predict a multinomial probability distribution (multiclass classification). Softmax axtivation function preduces a probability value between 0 to 1 for each class. The class with highest probability is the predicted class.

6. <b>What is the size of the input matrix?</b><br>
   input_dim = VOCAB_SIZE (no. of words in a dictionary) , output_dim = 128, input_length = MAX_LENGTH of sentence

7. <b>How many layers we used in the NN model? Which are they?</b><br>
   1 embedding input layer, 4 bilstm layer, 2 dense fully connected layer and 1 time distributed dense output layer

8. <b>How many gated memory units per layer in each domain?</b><br>
   The number of gated memory units used is as follows:<br/>
   Tourism Domain: 256, 128, 64<br/>
   Health Domain: 256, 128, 64<br/>
   News Domain: 512

9. <b>How many epoch is used to Training the model in each domain?</b><br>
   20 epochs in Health and Tourism domain and 60 in News domain.

10. <b>Which optimization applied to update weights among the different layers?</b><br>
    Adams optimizer with learning rate of 0.001

11. <b>What is the batch size of the model in each domain?</b><br>
    128

12. <b>Which loss function is used?</b><br>
    categorical crossentrophy for multiclass classification

13. <b>what is dense layer why we used?</b><br>
    The dense layer is a neural network layer that is connected deeply, which means each neuron in the dense layer receives input from all neurons of its previous layer. The output generated by the dense layer is an 'n' dimensional vector. Thus, dense layer is basically used for changing the dimensions of the vector.

14. <b>What is the dropout function and why we used it?</b><br>
    Dropout is a technique where randomly selected neurons are ignored during training. They are dropped-out randomly. This means that their contribution to the activation of downstream neurons is temporally removed on the forward pass and any weight updates are not applied to the neuron on the backward pass.
    Dropout is a technique used to prevent a model from overfitting and hence it improves accuracy.

15. <b>What is the value of dropout?</b><br>
    Can be anything between 0 and 1 (usually 0.2-0.5). I have used 0.25 for our model.

16. <b>How to calculate the number of parameters for each layer.</b><br>
    For a single hidden layer, number of parameters = connections between layers + biases in every layer (hiden + output layers) = (i×h + h×o) + (h+o) where,
    i= input size
    h= size of hidden layer (number of neurons in the hidden layer)
    o= output size (number of neurons in the output layer)

17. <b>How many sentences are trained in each domain??</b><br>
    35k in Health and 39k in Tourism.

18. <b>Kindly Draw graphs for the Performance (or any others) of model in each domain. (accuracy, precision, recall, and F-measure)</b><br>
Health domain:<br>

loss:
<div align="center">
    <img src="https://user-images.githubusercontent.com/58647922/124499695-159bae80-dddc-11eb-9585-efdd64bba311.png" height=400 width=600>
</div>

 accuracy:
<div align="center">
    <img src="https://user-images.githubusercontent.com/58647922/124499714-1c2a2600-dddc-11eb-93e3-017b9e0687df.png" height=400 width=600>
</div>
 
 Confusion matrix:
 <div align="center">
    <img src="https://user-images.githubusercontent.com/58647922/124499765-2fd58c80-dddc-11eb-91b0-b8beb0639f4e.png" height=400 width=700>
</div>
 
 Classification report:
 <div align="center">
    <img src="https://user-images.githubusercontent.com/58647922/124501820-e25b1e80-dddf-11eb-94f1-4c23b701526c.png" height=300 width=600>
</div>

Tourism Domain:<br>

loss:
<div align="center">
    <img src="https://user-images.githubusercontent.com/58647922/124500787-00c01a80-ddde-11eb-9ff6-601686db56be.png" height=400 width=600>
</div>

 accuracy:
<div align="center">
    <img src="https://user-images.githubusercontent.com/58647922/124500802-087fbf00-ddde-11eb-836d-a31954c3546f.png" height=400 width=600>
</div>
 
 Confusion matrix:
 <div align="center">
    <img src="https://user-images.githubusercontent.com/58647922/124502224-ae342d80-dde0-11eb-8463-efd8bedffd34.png" height=400 width=700>
</div>

Classification report:
 <div align="center">
    <img src="https://user-images.githubusercontent.com/58647922/124501241-cdca5680-ddde-11eb-97fc-698d79860d3b.png" height=300 width=600>
</div>
<br>
19. <b>Which technique use in the embedding layer?</b><br>
one-hot encoding

# Workflow:

 <div align="center">
    <img src="https://user-images.githubusercontent.com/58647922/124346449-7ec4cb80-dbfc-11eb-8e56-f91c9c364fa4.png">
</div>
