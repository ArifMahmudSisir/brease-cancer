import os
import numpy as np
import matplotlib.pyplot as plt

# file_path = "D:\DOWNLAODs\Thermal_Images_for_Breast_Cancer_Diagnosis_DMR-IR (1)\Imagens e Matrizes da Tese de Thiago Alves Elias da Silva\Desenvolvimento da Metodologia\SAUDAGòá++VEIS\42\Matrizes"


def process_file(file_path):
    # Load matrix from text file
    matrix = np.loadtxt(file_path)

    # Display the image
    plt.imshow(matrix, cmap='gray')  # Assuming it's a grayscale image
    plt.axis('off')  # Turn off axis labels


    # Optional: Save the image to a file
    output_image_path = file_path.replace('.txt', '_.jpg')
    plt.savefig(output_image_path)
    # plt.show()


def process_folder(folder_path):
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if it's a file (not a directory)
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            # Process the file
            print(f'Processing file: {file_path}')
            process_file(file_path)


if __name__ == "__main__":
    folder_path = 'C:\\Users\\sisir\\Downloads\\DATASET\\SICK'  # Replace with your folder path
    process_folder(folder_path)
