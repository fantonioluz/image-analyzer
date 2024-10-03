
# Analisador de Lotes - Classificação de Imagens de Lotes Ocupados e Vazios

Este projeto utiliza redes neurais convolucionais (CNN) para classificar imagens de satélite de terrenos, identificando e contando quantos lotes estão ocupados e quantos estão vazios. O modelo é baseado na arquitetura pré-treinada VGG16, aprimorado com camadas personalizadas para realizar a tarefa de classificação binária.

A interface do usuário permite o upload de múltiplas imagens, além de possibilitar a especificação do número de lotes verticais e horizontais para cada imagem. A aplicação processa cada imagem recortando os lotes e retornando o número de lotes vazios e ocupados.

## Funcionalidades

- **Classificação de lotes**: Identifica automaticamente se um lote está ocupado ou vazio a partir de imagens de satélite.
- **Upload múltiplo de imagens**: Permite o upload de várias imagens para análise simultânea.
- **Agrupamento de imagens**: Imagens com o mesmo formato de lote podem ser agrupadas para agilizar o processo de análise.
- **Interface intuitiva**: Desenvolvido com **Flask** e estilizado com **Tailwind CSS** para uma experiência visual agradável e funcional.
- **Modelo treinado**: O modelo VGG16 foi treinado e adaptado para esta tarefa de classificação.

## Estrutura do Projeto

```bash
├── app/
│   ├── __init__.py
│   ├── identificador.py   # Script de processamento das imagens
│   ├── routes.py          # Rotas Flask
│   ├── uploads/           # Diretório para armazenar as imagens temporárias
├── models/
│   ├── modelo_vgg16_melhorado.keras   # Modelo treinado
├── templates/
│   └── index.html         # Frontend da aplicação
├── static/
│   └── (Tailwind CSS e outros arquivos estáticos)
├── README.md
├── run.py                 # Script principal para rodar o servidor Flask
├── requirements.txt       # Dependências do projeto
└── venv/                  # Ambiente virtual Python (não incluído no Git)
```

## Requisitos

Para rodar o projeto, você precisará das seguintes dependências:

- Python 3.8+
- Flask
- TensorFlow
- Keras
- OpenCV
- Pillow (PIL)
- Tailwind CSS

Todas as dependências podem ser instaladas usando o `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Configuração e Execução

### Passos para rodar o projeto localmente:

1. **Clone o repositório**:

   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/fantonioluz/image-analyzer.git)
   cd image-analyzer
   ```

2. **Crie e ative um ambiente virtual** (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scriptsctivate  # Windows
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Coloque o arquivo do modelo na pasta `models/`**:
   - Se o arquivo do modelo não estiver no repositório, faça o download do modelo treinado [aqui](link-para-o-modelo) e coloque-o no diretório `models/`.

5. **Execute o servidor Flask**:

   ```bash
   python run.py
   ```

   O servidor será iniciado e poderá ser acessado em `http://127.0.0.1:5000/`.

6. **Interaja com a interface**:
   - Acesse a interface no navegador, faça upload das imagens, insira as quantidades de lotes verticais e horizontais, e clique em "Analisar Imagens" para obter os resultados.

7. **Limpeza automática**:
   - O diretório de uploads será automaticamente limpo ao encerrar a aplicação para garantir que não haja arquivos temporários residuais.

## Estrutura do Modelo

O modelo VGG16 foi pré-treinado no dataset **ImageNet** e, posteriormente, adaptado para a classificação de lotes ocupados e vazios. O modelo foi ajustado com camadas adicionais de classificação e regularização (Dropout), sendo treinado em imagens de terrenos para realizar uma predição binária:

- **Lote ocupado**: Valor de saída maior que 0.5.
- **Lote vazio**: Valor de saída menor ou igual a 0.5.

## Possíveis Melhorias

- Ajustar o modelo para obter uma melhor taxa de acerto.
- Implementar caching para acelerar o processamento de imagens já analisadas anteriormente.
- Adicionar suporte para mais formatos de imagens e ajustes automáticos de resolução.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
