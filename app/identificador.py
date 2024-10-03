import cv2
import numpy as np
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing.image import img_to_array # type: ignore
from PIL import Image

# Carregar o modelo treinado
model = load_model('models\modelo_vgg16_melhorado.keras')

def process_image(image_path, num_lotes_horizontal, num_lotes_vertical):
    # Carregar a imagem de satélite
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Erro ao carregar a imagem: {image_path}")
        return 0, 0
    
    try:
        image = Image.open(image_path)
        
        if image.mode == 'RGBA':
            image = image.convert('RGB')
        image = np.array(image)
    except Exception as e:
        print(f"Erro ao carregar a imagem: {image_path}, erro: {str(e)}")
        return
    
    
    # Dimensões da imagem e definição da quantidade de lotes
    height, width, _ = image.shape
    lote_height = height // num_lotes_vertical
    lote_width = width // num_lotes_horizontal

    # Contadores para lotes vazios e ocupados
    vazio_count = 0
    ocupado_count = 0

    # Percorrer cada "lote" na imagem
    for i in range(num_lotes_vertical):
        for j in range(num_lotes_horizontal):
            # Recortar a subimagem correspondente ao lote
            lote = image[i*lote_height:(i+1)*lote_height, j*lote_width:(j+1)*lote_width]
            
            # Redimensionar a imagem para o tamanho esperado pelo modelo
            lote_resized = cv2.resize(lote, (224, 224))
            
            # Preparar a imagem para o modelo
            lote_array = img_to_array(lote_resized) / 255.0
            lote_array = np.expand_dims(lote_array, axis=0)
            
            # Fazer a predição
            prediction = model.predict(lote_array)
            
            # Contar como vazio ou ocupado baseado na predição
            if prediction[0][0] > 0.5:  # Se a predição for maior que 0.5, considera "ocupado"
                vazio_count += 1
            else:  # Caso contrário, "vazio"
                ocupado_count += 1

    print(f"Resultado para {image_path}: Lotes vazios={vazio_count}, Lotes ocupados={ocupado_count}")
    return vazio_count, ocupado_count
