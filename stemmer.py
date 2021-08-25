stemWords = {}

def readStemWords():
    '''
        Reads the words from the stem words list and transforms the data into usable format
     '''
    global stemWords
    with io.open("word_list_marathi.txt", encoding='utf-8') as textFile:
        index = 0
        for line in textFile:
            line = line.strip()
            if len(line) > 0:
                index += 1
                wordEndIndex = line.find(">")
                word = line[2:wordEndIndex]
                line = line[wordEndIndex + 1:]
                baseEndIndex = line.find("]")
                base = line[1:baseEndIndex].strip()
                line = line[baseEndIndex + 1:]
                stem = None
                if len(base) >= 0:
                    stemEndIndex = base.find('-')
                    if stemEndIndex > 0:
                        stem = base[:stemEndIndex]

                valid = line[line.find("(")+ 1: line.find(")")].strip()
                if valid == "0":
                    continue
                line = line[line.find("{") + 1: line.find("}")].strip()
                related = []
                if len(line) > 0:
                    split = line.split(",")
                    for s in split:
                        related.append(s[:s.find("|")])
                if stem == None and len(related) > 0:
                    stem = related[0]
                if stem != None:
                    stemWords[word] = {}
                    stemWords[word]["stem"] = stem
                    stemWords[word]["related"] = related


def removeCase(word):
    '''
    :param word: word to be reduced its stem
    :return: stem of the word
    '''
    word_length = len(word) - 1
    if word_length > 5:
        suffix = "शया"
        if word.endswith(suffix):
            return word[:-len(suffix)]

    if word_length > 4:
        suffix = "शे"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "शी"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "चा"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ची"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "चे"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "हून"
        if word.endswith(suffix):
            return word[:-len(suffix)]

    if word_length > 3:
        suffix = "नो"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "तो"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ने"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "नी"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ही"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ते"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "या"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ला"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ना"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ऊण"
        if word.endswith(suffix):
            return word[:-len(suffix)]

    if word_length > 2:
        suffix = " े"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ी"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "स"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ल"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ा"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "त"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "म"
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word


def removeNoGender(word):
    '''
    :param word:
    :return:
    '''
    global stemWords
    orig = word
    if word in stemWords:
        return stemWords[word]["stem"]
    word_length = len(word) - 1

    if word_length > 5:
        suffix = " ुरडा"
        if word.endswith(suffix):
            return word[:-len(suffix)]

    if word_length > 4:
        suffix = "ढा"
        if word.endswith(suffix):
            return word[:-len(suffix)]

    if word_length > 3:
        suffix = "रु"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "डे"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ती"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ान"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ीण"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "डा"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "डी"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "गा"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ला"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ळा"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "या"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "वा"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ये"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "वे"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ती"
        if word.endswith(suffix):
            return word[:-len(suffix)]

    if word_length > 2:
        suffix = "अ"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " े"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ि "
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ु"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ौ"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ै"
        if word.endswith(suffix):
            return word[:-len(suffix)]

        suffix = " ा"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ी"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ू"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "त"
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word


def stemmerMarathi(words):
    return [removeNoGender(removeCase(word)) for word in words]


def stemWord(word):
    return removeNoGender(removeCase(word))

# sentence = "अंबाला जिल्ह्याचे प्रशासकीय केंद्र अंबाला शहरात आहे ."
# for word in sentence.split(" "):
#     print(stemWord(word))