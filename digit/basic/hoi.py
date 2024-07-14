from PIL import Image, ImageDraw
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Function to generate image of a number
def generate_number_image(number):
    # Create a blank white image
    image = Image.new('L', (28, 28), color='white')
    draw = ImageDraw.Draw(image)
    
    # Draw the number on the image
    draw.text((10, 10), str(number), fill='black')
    
    return image

# Generate images for numbers 0 to 9
X = []
y = []

for number in range(10):
    image = generate_number_image(number)
    X.append(np.array(image).flatten())
    y.append(number)

# Convert lists to numpy arrays
X = np.array(X)
y = np.array(y)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train SVM model
model = SVC(kernel='linear', C=1.0, gamma='auto')  # Linear SVM
model.fit(X_train, y_train)

# Function to display image and predict number
def display_and_predict(input_number):
    # Generate input image
    input_image = generate_number_image(input_number)
    input_image_array = np.array(input_image).reshape(28, 28)  # Reshape for display
    
    # Display input image
    plt.imshow(input_image_array, cmap='gray')
    plt.axis('off')
    plt.show()
    
    # Predict using the trained model
    input_image_flattened = np.array(input_image).flatten()
    predicted_number = model.predict([input_image_flattened])[0]
    print(f"Predicted number: {predicted_number}")
    return predicted_number

# Example usage: Predicting a number (replace 'input_number' with your input)