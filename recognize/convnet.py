### IMPORT PACKAGES
# USE FOR IMAGE I/O
import cv2
# USE FOR DATA PREPROCESS
import pandas as pd
import numpy as np
# USE FOR DATA PATH & VERBOSE
import os, warnings
# USE FOR MODEL BUILT
import numpy as np
import tensorflow as tf
import keras
warnings.filterwarnings("ignore")

# PARAMETERS FOR TEST DATA
model_path = "recognize/keras_model"

### TEST DATA PREPROCESS
# DEFINE FUNCTION : TEST DATA PREPROCESS
def preprocess_test_data(test_data_path: str) -> pd.DataFrame:
    if test_data_path[0] == "/":
        test_data_path = test_data_path[1:]
    else:
        pass
    test_data_path = os.path.abspath(test_data_path)
    # CONVERT IMAGE TO 784(28*28) GRAYSCALE PIXEL DATAFRAME -> COLOR MAY NOT BE IMPORTANT HERE
    df = pd.DataFrame(columns=range(784)).add_prefix("pixels_")
    if test_data_path.endswith((".jpg", ".png")):
        try:
            r_image = cv2.imread(test_data_path) # 只吃絕對路徑
            numpy_image = cv2.cvtColor(r_image, cv2.COLOR_BGR2GRAY)
            image = cv2.resize(numpy_image, (28, 28)).astype(np.float32)
            image = image.reshape(-1)
        except Exception as e:
            print(f"[FILE「{test_data_path}」ENCOUNTERED ERROR]\n{e}")
        df.loc[0, "pixels_0":] = image
    else:
        print("請輸入 .jpg 或 .png 格式的照片")
        return None
    # RESHAPE FROM DATAFRAME TO 3-D MATRIX
    data_x = df.values[:, :]
    height = width = int(pow(data_x.shape[1], 0.5))
    data_x = data_x.reshape(data_x.shape[0], 1, height, width).astype("float32")
    # NORMALIZE DATA FROM [0, 255] TO [0, 1]
    data_x_np = data_x / 255.0
    return data_x

### save & load model 的版本一定要一致
### BUILD CONVNETS
# DEFINE CLASS : BUILD CONVNETS
class convnets:
    def __init__(self,
                 train_x: np.ndarray,
                 train_y: np.ndarray,
                 valid_x: np.ndarray,
                 valid_y: np.ndarray) -> None:
        self.train_x = train_x
        self.train_y = train_y
        self.valid_x = valid_x
        self.valid_y = valid_y
        self.CATEGORIES = len(self.train_y[0])
    def save_model(self) -> None:
        # SERIALIZE（序列化）MODEL TO JSON
        model_json = self.model.to_json()
        with open("model.json", "w") as json_file:
            json_file.write(model_json)
        # SERIALIZE WEIGHTS TO HDF
        self.model.save_weights("model_weights.h5")
    def predict(self,
                test_x,
                model_path: str=model_path) -> str:
        # SOLVE CPU VERSION ONLY SUPPORT `NHWC`
        tf.keras.backend.set_image_data_format('channel_first')
        test_x = np.moveaxis(test_x, 0, 2)
        try:
            # LOAD PRETRAINED MODEL，LOADING KERAS IS BETTER
            loaded_model = keras.models.load_model(os.path.join(model_path, "model.keras"))
            # LOAD WEIGHTS INTO NEW MODEL
            loaded_model.load_weights(os.path.join(model_path, "model_weights.h5"))
        except:
            print("LOAD MODEL FAILED.")
        try:
            # GET MODEL PREDICTIONS
            prediction = loaded_model.predict(test_x)
            # SINCE PREDICTIONS ARE LIKE ONE-HOT ENCODED, CONVERT THEM TO LABELS
            pred_id = np.argmax(prediction, axis=1)
        except:
            print("PREDICT FAILED.")
        id2label = {1: "狗狗", 0: "貓咪"} #  SORT BY ALPHABET
        pred = id2label[pred_id[0]]
        return pred
