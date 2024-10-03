import os
import shutil
import atexit
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from app.identificador import process_image  # Importa o código de análise

app = Flask(__name__)

UPLOAD_FOLDER = 'app/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_images():
    try:
        images = request.files.getlist('images')
        vertical = int(request.form.get('vertical'))
        horizontal = int(request.form.get('horizontal'))
        
        if not images:
            return jsonify({'error': 'Nenhuma imagem enviada'}), 400
        
        total_vazio_count = 0
        total_ocupado_count = 0

        for image in images:
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)

            print(f"Processando a imagem: {image_path}")  # Log para depurar
            
            # Processa a imagem usando o modelo
            vazio_count, ocupado_count = process_image(image_path, horizontal, vertical)
            print(f"Resultado para {image.filename}: Lotes vazios={vazio_count}, Lotes ocupados={ocupado_count}")  # Log para depurar

            total_vazio_count += vazio_count
            total_ocupado_count += ocupado_count

        return jsonify({
            'lotes_vazios': total_vazio_count,
            'lotes_ocupados': total_ocupado_count
        })
    
    except Exception as e:
        print(f"Erro durante a análise das imagens: {e}")  # Log de erro detalhado no terminal
        return jsonify({'error': str(e)}), 500

def clear_upload_folder():
    """Função que apaga todo o conteúdo da pasta uploads."""
    try:
        shutil.rmtree(UPLOAD_FOLDER)  # Remove a pasta uploads e tudo dentro dela
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Cria novamente a pasta vazia
        print("Pasta uploads limpa com sucesso.")
    except Exception as e:
        print(f"Erro ao limpar a pasta uploads: {e}")

# Registro a função clear_upload_folder para ser chamada quando a aplicação for desligada
atexit.register(clear_upload_folder)

if __name__ == '__main__':
    app.run(debug=True)
