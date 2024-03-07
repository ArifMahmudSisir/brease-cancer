import scipy
import os
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

# Define augmentation parameters
datagen = ImageDataGenerator(
    rotation_range=15,  # Degree range for random rotations
    width_shift_range=0.2,  # Width shift range as a fraction of total width
    height_shift_range=0.2,  # Height shift range as a fraction of total height
    rescale=1./255,  # Rescale pixel values to [0, 1]
    shear_range=0.2,  # Shear intensity (radians)
    zoom_range=0.2,  # Zoom range
    horizontal_flip=True,  # Enable horizontal flipping
    fill_mode='nearest',  # Strategy for filling missing pixels after transformations
    data_format='channels_last',  # Image data format
    brightness_range=[0.5, 1.5]  # Random brightness range
)

# Specify input and output directories
input_dir = 'C:\\Users\\sisir\\Downloads\\Augmented\\dataset23\\Sick'  # Replace with your input folder name
output_dir = 'C:\\Users\\sisir\\Downloads\\Augmented\\fndt\\\Sick'  # Output folder for augmented images

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
d=0
# Iterate through files in the input directory
for filename in os.listdir(input_dir):
    img_path = os.path.join(input_dir, filename)
    img = load_img(img_path)  # Load the image
    x = img_to_array(img)  # Convert image to NumPy array
    x = x.reshape((1,) + x.shape)  # Reshape for the generator


    d=d+1
    print("image Number: " + str(d) + " is done")
    # Generate augmented images
    i = 0
    for batch in datagen.flow(x, batch_size=1, save_to_dir=output_dir, save_prefix="aug_", save_format='png'):
        i += 1
        if i > 200:  # Generate one augmented image per original image

          break
