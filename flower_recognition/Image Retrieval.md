# Image Retrieval

### Step 1. Image feature extraction

Using the last fully connected layer of a CNN classification model, e.g., VGG19 to extract the features of an image

Source code: `extract_features_vgg19.py`

```python
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

```



1. Install Keras: 

   - Follow this instruction: https://keras.io/#installation
   - Note: To install a backend engine first, --> TensorFlow

2. Reference: https://keras.io/applications/#applications

3. Run: `python extract_features_vgg19.py` to extract 1x4096 feature vector of an image

   - Note 1: `target_size=(224, 224)` already resizes the input image

   - Note 2: It's possible to extract multiple images using one `model.predict`

      

```python
def load_images_from_folder(imglist, img_size=IMG_SIZE):
    Xs = []
    for img in imglist:
        img_path = os.path.join(AVA_FOLDER, img)
        im = image.load_img(
            img_path,
            target_size=(img_size, img_size)
        )
        im = image.img_to_array(im)
        # im = im.transpose((2, 0, 1))
        Xs.append(im)
    Xs = np.asarray(Xs)
    return Xs

#set x_ids here?
x_ids = []
x_imgs = load_images_from_folder(x_ids, img_size=224)
x_imgs = preprocess_input(x_imgs)
features = model.predict(x_imgs)

#Use cPickle to dump the features to file - for future use
 cPickle.dump(x_train_features, open("x_vgg_features.pickle", "wb"))
```



### Step 2: Retrieval

Many algorithms but let's use K-nearest neighbors from `sklearn` library.

Ref: http://scikit-learn.org/stable/modules/neighbors.html#finding-the-nearest-neighbors



```python
>>> from sklearn.neighbors import NearestNeighbors
>>> import numpy as np
>>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
>>> nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
>>> distances, indices = nbrs.kneighbors(X)
>>> indices                                           
array([[0, 1],
       [1, 0],
       [2, 1],
       [3, 4],
       [4, 3],
       [5, 4]]...)
>>> distances
array([[0.        , 1.        ],
       [0.        , 1.        ],
       [0.        , 1.41421356],
       [0.        , 1.        ],
       [0.        , 1.        ],
       [0.        , 1.41421356]])

```

