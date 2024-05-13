import cv2
import numpy as np
import os
from skimage.feature import graycomatrix, graycoprops

def calculate_structural_features(image):
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(largest_contour)
    perimeter = cv2.arcLength(largest_contour, True)
    return area, perimeter

def calculate_statistical_features(image):
    mean_val = np.mean(image)
    std_dev = np.std(image)
    variance = np.var(image)
    range_pixel = np.ptp(image)
    return mean_val, std_dev, variance, range_pixel

def calculate_glcm_features(image):
    glcm = graycomatrix(image, [1], [0], 256, symmetric=True, normed=True)
    contrast = graycoprops(glcm, 'contrast')[0, 0]
    dissimilarity = graycoprops(glcm, 'dissimilarity')[0, 0]
    homogeneity = graycoprops(glcm, 'homogeneity')[0, 0]
    energy = graycoprops(glcm, 'energy')[0, 0]
    return contrast, dissimilarity, homogeneity, energy

directory = "D:/Desktop/CG/Atividade7/MAIUSCULAS"
output_file = "D:/Desktop/CG/Atividade7/resultados_imagens.txt"
with open(output_file, "w") as file:
    for filename in os.listdir(directory):
        if filename.lower().endswith('.pgm'):
            img_path = os.path.join(directory, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            
            area, perimeter = calculate_structural_features(img)
            mean_val, std_dev, variance, range_pixel = calculate_statistical_features(img)
            contrast, dissimilarity, homogeneity, energy = calculate_glcm_features(img)
            
            class_label = filename.split('.')[0][0]
            
            file.write(f"{class_label} {area:.2f} {perimeter:.2f} {mean_val:.2f} {std_dev:.2f} {variance:.2f} {range_pixel:.2f} {contrast:.2f} {dissimilarity:.2f} {homogeneity:.2f} {energy:.2f}\n")

print(f"Os resultados foram salvos em '{output_file}'")