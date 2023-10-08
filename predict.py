import keras
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# fonction de prédiction
#Etant fournie le chemin du modèle avec celui du tokenizer il applique le modèle sur le text
#Pour fournir comme résultat si la sentence était positive ou négative et sa proba
def predict_method(modelPath, tokenizerPath, text):
    with open(tokenizerPath, 'rb') as token:
        tokenizer = pickle.load(token)

    model = keras.models.load_model(modelPath)
    #Traitement du text
    textseq = tokenizer.texts_to_sequences([text])
    textpad = pad_sequences(textseq, maxlen=1000)
    
    proba = model.predict(textpad)[0][0]
    if proba >= 0.5:
        sentiment = "positive"
    else:
        sentiment = "negative"

    print("this sentence is {} with a probability of {}".format(sentiment, proba))



phrase = input("Enter your sentence:")

predict_method("lstm_model.h5", "tokenizer.pickle", phrase)
