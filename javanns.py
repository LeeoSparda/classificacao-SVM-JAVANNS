import cv2
import numpy as np
import os
from skimage.feature import graycomatrix, graycoprops

# Função para calcular características estruturais da imagem
def calculate_structural_features(image):
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(largest_contour)
    perimeter = cv2.arcLength(largest_contour, True)
    return area, perimeter

# Função para calcular características estatísticas da imagem
def calculate_statistical_features(image):
    mean_val = np.mean(image)
    std_dev = np.std(image)
    variance = np.var(image)
    range_pixel = np.ptp(image)
    return mean_val, std_dev, variance, range_pixel

# Função para calcular características GLCM da imagem
def calculate_glcm_features(image):
    glcm = graycomatrix(image, [1], [0], 256, symmetric=True, normed=True)
    contrast = graycoprops(glcm, 'contrast')[0, 0]
    dissimilarity = graycoprops(glcm, 'dissimilarity')[0, 0]
    homogeneity = graycoprops(glcm, 'homogeneity')[0, 0]
    energy = graycoprops(glcm, 'energy')[0, 0]
    return contrast, dissimilarity, homogeneity, energy

# Função para escrever os dados no formato SVM
def write_svm_format(data, class_label, output_file):
    with open(output_file, "a") as file:
        # Formatação dos dados como linha no formato SVM
        line = f"{class_label} " + " ".join(f"{i+1}:{feature:.2f}" for i, feature in enumerate(data))
        file.write(line + "\n")

# Função para escrever os dados no formato JavANNs
def write_javanns_format(data, class_label, output_file):
    with open(output_file, "a") as file:
        # Formatação dos dados como linha no formato JavANNs
        line = ",".join(f"{feature:.2f}" for feature in data) + f",{class_label}"
        file.write(line + "\n")

# Diretório contendo as imagens
directory = "C:/Users/Leonardo Borges/Desktop/CG/Atividade7/atividade/MAIUSCULAS"
# Arquivo de saída para SVM
output_file_svm = "C:/Users/Leonardo Borges/Desktop/CG/Atividade7/atividade/svm_resultados.txt"
# Arquivo de saída para JavANNs
output_file_javanns = "C:/Users/Leonardo Borges/Desktop/CG/Atividade7/atividade/javanns_resultados.txt"

# Loop sobre os arquivos no diretório
for filename in os.listdir(directory):
    if filename.lower().endswith('.pgm'):
        # Caminho completo da imagem
        img_path = os.path.join(directory, filename)
        # Carrega a imagem em escala de cinza
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        
        # Calcula características estruturais, estatísticas e GLCM da imagem
        area, perimeter = calculate_structural_features(img)
        mean_val, std_dev, variance, range_pixel = calculate_statistical_features(img)
        contrast, dissimilarity, homogeneity, energy = calculate_glcm_features(img)
        
        # Extrai a classe da imagem (presumindo que o primeiro caractere do nome do arquivo
        # representa a classe)
        class_label = filename.split('.')[0][0]
        # Concatena todas as características em uma lista
        features = [area, perimeter, mean_val, std_dev, variance, range_pixel, contrast, dissimilarity, homogeneity, energy]
        
        # Escreve os dados nos arquivos de saída nos formatos SVM e JavANNs
        write_svm_format(features, class_label, output_file_svm)
        write_javanns_format(features, class_label, output_file_javanns)

# Mensagem de conclusão
print(f"Os resultados foram salvos em '{output_file_svm}' para SVM e '{output_file_javanns}' para JavANNs.")
