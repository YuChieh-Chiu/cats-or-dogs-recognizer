# CATS OR DOGS RECOGNIZER

> ![cmd-svg](./readme_source/terminal-fill.svg) `Django` + ![gear-svg](./readme_source/gear-wide-connected.svg) `Convnets` = ![window-svg](./readme_source/window-fullscreen.svg) `Cats or Dogs Recognizer Website`

## Project Overview
> [!IMPORTANT]
> In this project, I have developed a website based on the `Django` framework to demonstrate my `Convnets` model.

> Users can upload photos of cats and dogs in `JPG` or `PNG` format.
The website will then call a `Convnets` model that I have trained to identify whether the animal in the uploaded image is a cat or a dog, and return the result. 
Afterwards, users can provide feedback indicating whether the identification result was correct or incorrect. 
The website collects all user feedback history and presents the current model's accuracy and recall rates for identifying cats and dogs separately.

## Model Overview
> [!IMPORTANT]
> After validation using around 2,000 cat photos and 2,000 dog photos, **the accuracy of the model is approximately 92%**.

> This is a `Convnets` model **trained on a balanced dataset of approximately 8,000 cat photos and 8,000 dog photos**. 
The model consists of a total of eighteen layers, including the **Input Layer, Data Augmentation Layer, BatchNormalization Layer, Conv2D Layer, MaxPool2D Layer, Dropout Layer, Flatten Layer, and Dense Layer**.

## Note
> [!NOTE]
> This project can only run in `GPU supported` environment, since the Convnets model used in this project is in data_type `NCHW`, but the `CPU only` environment can only support data_type `NHWC`.
