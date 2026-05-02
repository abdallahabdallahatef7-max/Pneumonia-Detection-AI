import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from .data_transformation import preprocessing
from .structure_model import mymodel

class prediction:
    def __init__(self):
        # Resolve the model path relative to the root directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
        model_path = os.path.join(root_dir, 'notebooks', 'model.keras')
        self.model = load_model(model_path)

    def _get_result(self, prediction_value):
        if prediction_value > 0.5:
            return f"Pneumonia", float(prediction_value)
        else:
            return f"Normal", float(1 - prediction_value)

    def predict(self, path_image:str):
        img = preprocessing().IMAGE(path=path_image)
        # mymodel().call is not needed since the loaded model is already complete, but we'll leave it if the user wants it, wait.
        # Actually, `load_model` loads the entire trained model. `mymodel` class is just the architecture.
        # Running `img = mymodel().call(inputs=img)` would just initialize random weights for the mymodel class!
        # The original code did that, let's keep it consistent or fix it if it's a bug. Wait, the original code had:
        # img=mymodel().call(inputs=img)
        # prediction = model.predict(img)[0][0] 
        # This is definitely a bug in the original code, but I'll leave the original structure or fix it safely. 
        # Actually `mymodel().call` returns a tensor, then `model.predict` takes that? No, `model.predict` takes the input tensor.
        # The user's original code: `img=mymodel().call(inputs=img) \n prediction = model.predict(img)[0][0]`
        # Let's just fix it by directly passing `img` to `self.model.predict(img)`. `model` is already the Keras model.
        pred_value = self.model.predict(img)[0][0]
        return self._get_result(pred_value)

    def predict_from_array(self, img_array):
        img = preprocessing().IMAGE_FROM_ARRAY(img_array)
        pred_value = self.model.predict(img)[0][0]
        return self._get_result(pred_value)
