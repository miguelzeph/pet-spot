from settings import UPLOAD_FOLDER, MODEL_PATH, config_tensorflow
# Env vars
config_tensorflow()

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

tf.config.set_visible_devices([], 'GPU')  # Desabilita o uso de GPU


# Carregar o modelo TFLite com o shape de entrada fixo
interpreter = tf.lite.Interpreter(model_path=MODEL_PATH)
interpreter.allocate_tensors()

# Obtenha detalhes de entrada e saída
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def predict_animal_species(path: str):
    """
    Predict the species of an animal from an image file using TFLite.
    
    Args:
        image_name (str): Nome do arquivo da imagem na pasta './image_tests/'.

    Returns:
        dict: Um dicionário com nomes de espécies como chaves e as probabilidades de predição como valores.
    """
    # Carregar e preparar a imagem
    sample_image = tf.keras.preprocessing.image.load_img(f'{UPLOAD_FOLDER}/{path}', target_size=(224, 224))
    plt.imshow(sample_image)

    # Converter a imagem para array e expandir dimensões
    sample_image = tf.keras.preprocessing.image.img_to_array(sample_image)
    sample_image = np.expand_dims(sample_image, axis=0).astype(np.float32)

    # Pré-processar a imagem para o EfficientNet
    sample_image = tf.keras.applications.efficientnet.preprocess_input(sample_image)

    # Definir a imagem como entrada para o modelo TFLite
    interpreter.set_tensor(input_details[0]['index'], sample_image)
    
    # Rodar a inferência
    interpreter.invoke()

    # Extrair os resultados da inferência
    predictions = interpreter.get_tensor(output_details[0]['index'])

    # Formatar a saída como dicionário
    output = {
        'birds':   predictions[0][0],
        'cats':    predictions[0][1],
        'dogs':    predictions[0][2],
        'fishs':   predictions[0][3],
        'hamsters':predictions[0][4],
        'monkeys': predictions[0][5],
        'reptiles':predictions[0][6],
    }
    return output

