from keras.applications.vgg19 import VGG19
from keras.preprocessing import image
from keras.applications.vgg19 import preprocess_input
from keras.models import Model
import numpy as np

base_model = VGG19(weights='imagenet')

model = Model(
            inputs=base_model.input,
            outputs=base_model.get_layer('fc2').output
            )

img_path = 'images/test.jpg'
img = image.load_img(
            img_path,
            target_size=(224, 224)
            )
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

features = model.predict(x)

print features.shape
print features
