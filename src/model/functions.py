import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from settings import UPLOAD_FOLDER, MODEL_PATH

model = tf.keras.models.load_model(MODEL_PATH)

def pred(path):
    # Abrir IMG
    sample_image = tf.keras.preprocessing.image.load_img( f'{UPLOAD_FOLDER}/{path}',
    target_size=(224,224)
    )

    plt.imshow(sample_image)
    
    # Img to Array
    sample_image = tf.keras.preprocessing.image.img_to_array(sample_image)
    # Colocar no formado (1,224,224,3)
    sample_image = np.expand_dims(sample_image,axis=0)
    # Normalizar de acordo com o Resnet50
    sample_image = tf.keras.applications.efficientnet.preprocess_input(sample_image)
    # prever
    predictions = model.predict(sample_image)
    
    #return predictions
    
    saida = {
        'bird':   round(predictions[0][0],3),
        'cat':    round(predictions[0][1],3),
        'dog':    round(predictions[0][2],3),
        'fish':   round(predictions[0][3],3),
        'hamster':round(predictions[0][4],3),
        'monkey': round(predictions[0][5],3),
        'reptile':round(predictions[0][6],3),
    }
    return saida




