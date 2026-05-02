import cv2
import numpy as np

class preprocessing:
    def IMAGE(self,path):
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) 
        img = cv2.resize(img, (150, 150)) 
        img = img / 255.0 
        img = np.expand_dims(img, axis=-1) # Add channel dimension (150, 150, 1)
        img = np.expand_dims(img, axis=0) # Add batch dimension (1, 150, 150, 1)

        return img
        
    def IMAGE_FROM_ARRAY(self, img_array):
        if len(img_array.shape) == 3:
            img = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        else:
            img = img_array
        img = cv2.resize(img, (150, 150)) 
        img = img / 255.0 
        img = np.expand_dims(img, axis=-1) # Add channel dimension (150, 150, 1)
        img = np.expand_dims(img, axis=0) # Add batch dimension (1, 150, 150, 1)

        return img