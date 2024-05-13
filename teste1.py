import cv2
import numpy as np
import mahotas.features.texture as mht

def extract_features(image):
    # Extraindo características estruturais
    edges = cv2.Canny(image, 100, 200)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    structural_features = len(contours)  # Número de contornos encontrados

    # Extraindo estatísticas
    stats = cv2.connectedComponentsWithStats((image > 0).astype(np.uint8), 8, cv2.CV_32S)
    stats_features = stats[2][1:]  # Remover o primeiro elemento, que é o fundo

    # Extraindo características da GLCM
    textures = mht.haralick(image.astype(np.uint8))
    glcm_features = textures.mean(axis=0)
    
    return structural_features, stats_features, glcm_features

def process_image(image_path):
    # Lendo a imagem
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Extraia características
    structural_features, stats_features, glcm_features = extract_features(image)

    # Escreva os resultados em um arquivo de texto
    with open(image_path[:-4] + '_results.txt', 'w') as file:
        file.write("Imagem: {}\n".format(image_path))
        file.write("Características Estruturais: {}\n".format(structural_features))
        file.write("Estatísticas:\n")
        for i, stat in enumerate(stats_features):
            file.write("Região {}: {}\n".format(i, stat))
        file.write("Características da GLCM: {}\n".format(glcm_features))

    print("Resultados salvos em:", image_path[:-4] + '_results.txt')

image_path = "D:/Desktop/CG/Atividade7/B.png"
process_image(image_path)
