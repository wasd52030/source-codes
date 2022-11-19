from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from matplotlib import pyplot
from PIL import Image
import os

project_id = '2a04769a-dad8-441a-9a8d-f1d90abe5858' 
cv_key = 'c7544e23212440548b8cd7bb9fbf6dd6'
cv_endpoint = 'https://japaneast.api.cognitive.microsoft.com/' 

model_name = 'Iteration1' 
 
# Get the test images from the data/vision/test folder
test_folder = os.path.join('static')
test_images = os.listdir(test_folder)
 
# Create an instance of the prediction service
credentials = ApiKeyCredentials(in_headers={"Prediction-key": cv_key})
custom_vision_client = CustomVisionPredictionClient(endpoint=cv_endpoint, credentials=credentials)
 
# Create a figure to display the results
fig = pyplot.figure(figsize=(16, 8))
 
# Get the images and show the predicted classes for each one
print('Classifying images in {} ...'.format(test_folder))
for i in range(len(test_images)):
    # Open the image, and use the custom vision model to classify it
    image_contents = open(os.path.join(test_folder, test_images[i]), "rb")
    classification = custom_vision_client.classify_image(project_id, model_name, image_contents.read())
    # The results include a prediction for each tag, in descending order of probability - get the first one
    prediction = classification.predictions[0].tag_name
    print(type(classification.predictions[0]))
    # Display the image with its predicted class
 #   img = Image.open(os.path.join(test_folder, test_images[i]))
 #   a=fig.add_subplot(len(test_images)/3, 3,i+1)
 #   a.axis('off')
 #   imgplot = plt.imshow(img)
 #   a.set_title(prediction)
#plt.show()