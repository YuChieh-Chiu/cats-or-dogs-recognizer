Cats or Dogs Recognizer
===
> ![cmd-svg](./readme_source/terminal-fill.svg) `Django` + ![gear-svg](./readme_source/gear-wide-connected.svg) `Convnets` + ![cloud-svg](./readme_source/cloud-check-fill.svg) `Render` = ![window-svg](./readme_source/window-fullscreen.svg) `Cats or Dogs Recognizer Website`
---
![cats-and-dogs-image](https://images.unsplash.com/photo-1606098216818-40939b7c98ad?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

# Project Overview
> In this project, I have developed a website based on the `Django` framework. 
> Users can upload photos of cats and dogs in `JPG` or `PNG` format. 
> The website will then call a `Convolutional Neural Network` model that I have trained to identify whether the animal in the uploaded image is a cat or a dog, and return the result. 
> Afterwards, users can provide feedback indicating whether the identification result was correct or incorrect. 
> The website collects all user feedback history and presents the current model's accuracy and recall rates for identifying cats and dogs separately.

# Model Overview
> This is a `Convolutional Neural Network` model **trained on a balanced dataset of approximately 8,000 cat photos and 8,000 dog photos**. 
> The model consists of a total of eighteen layers, including the **Input Layer, Data Augmentation Layer, BatchNormalization Layer, Conv2D Layer, MaxPool2D Layer, Dropout Layer, Flatten Layer, and Dense Layer**.
> After validation using around 2,000 cat photos and 2,000 dog photos, **the accuracy of the model is approximately 92%**.

# Note
- This project can only run in `GPU supported` environment, since the Convolutional Neural Network model used in this project is in data_type `NCHW`, but the `CPU only` environment can only support data_type `NHWC`.
