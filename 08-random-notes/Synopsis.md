
# 1. Abstract


The focus of this master's project is on the development of a deep learning-based method for the semantic segmentation of drone imagery. Unmanned aerial vehicles (UAVs), which can swiftly and effectively collect data from the air, are being employed more and more in a wide range of industries. Semantic segmentation involves assigning a label or class to each pixel in an image, enabling detailed understanding of the scene depicted. In order to predict the class of each pixel in new photos, convolutional neural networks (CNN) are trained using tagged aerial photographs. Land use mapping, urban planning, and environmental monitoring are just a few of the applications that the model can be applied to once it has been trained and evaluated to performance criteria.


# 2. Introduction

A branch of artificial intelligence called machine learning involves teaching algorithms to spot patterns and draw conclusions from input data. It enables computers to develop their skills and perform better without explicit programming.Deep learning is a subfield of machine learning that is inspired by the structure and function of the neural networks of the human brain. Layers of interconnected nodes which form an artificial neural network are used to analyse and make decesions based on the input data. Deep learning algorithms are able to learn directly from the raw data, as opposed to standard machine learning methods, which depend on hand-crafted features and involve extensive preparation.This makes them particularly well-suited for tasks such as image recognition, natural language processing, and speech recognition, where the data is highly complex and structured. It has made tremendous advancements in areas like computer vision and natural language processing in recent years, where it has found exceptional success in a variety of applications. Deep learning, as a whole, is a fast developing area that has the potential to drastically alter how we interact with and understand data. Future advancements in machine learning and artificial intelligence are anticipated to depend heavily on it.

Computer vision is a field of artificial intelligence that focuses on enabling computers to interpret and comphrehend visual data from the world around them. In order to perform tasks like object recognition, picture segmentation, and scene interpretation, it is necessary to build algorithms and approaches that can analyse and comprehend images and videos. Deep learning techniques have contributed to significant advances in computer vision in recent years. Deep learning has enabled computers to learn and recognise patterns and features in images and videos in a manner similar to that of the human brain. This has resulted in significant advances in areas such as image classification and object detection, as well as the ability for computers to perform tasks like face recognition and autonomous driving. One such area of focus is segmentaion, specifically semantic segmentaion which is the focus of this project. 


### Segmentation
---
The process of dividing an image into multiple segments or regions, each of which corresponds to a different object or background in the image, is referred to as segmentation in computer vision. The goal of image segmentation is to simplify and/or change an image's representation into something more meaningful and easier to analyse. It is a critical step in many computer vision and image analysis tasks. It is frequently used as a preprocessing step for these tasks because it can help to simplify and make the data easier to work with. 

Object detection and image segmentation are two closely related computer vision tasks, but they differ significantly. Object detection is the process of detecting the presence and location of objects in an image or video, but it does not always distinguish between different instances of the same object. Image segmentation, on the other hand, involves splitting an image into many segments or areas, each of which corresponds to a different item or backdrop in the image. Image segmentation aims to simplify and/or transform an image's representation into something more relevant and easier to study. Image segmentation has a wide range of application. It is frequently used as a preprocessing step for these tasks because it can help to simplify and make the data easier to work with. Hence, object detection and image segmentation are closely related tasks, but they serve different purposes. Object detection is concerned with identifying the presence and location of objects in an image, while image segmentation is focused on dividing an image into distinct segments or regions.

Image segmentation can be used in object detection to identify and separate objects in an image, making it easier to recognize and classify them, in scene interpretation to comprehend the layout and structure of a scene by identifying and segmenting various objects and regions within an image, in image editing to select specific objects or regions in an image for manipulation. It is used immensly medical imaging and microscopists,where it is used to identify and segment different structures in images of the human body, such as cells, organs, tumours, and blood vessels. It is used in Robotics, to  perceive and understand their surroundings, by identifying and segmenting objects and obstacles in the environment. Recent developments in augemented reality applies segmentation to identify and segment specific objects or regions in the real world and overlay digital content on top of them, thereby enabling augmented reality applications.

Image segmentation can be said to be of two types, Instance Segmentation and Semantic Segmentation. Instance segmentation entails segmenting each instance of an object independently in addition to identifying its presence and location within an image. As a result, instance segmentation is able to recognise and differentiate between several instances of the same object and can offer a unique mask for each instance. In contrast, semantic segmentation involves classifying each pixel in an image into a predefined set of classes without necessarily distinguishing between different instances of the same class. Overall, because it can identify and segment individual instances of objects, instance segmentation provides a more detailed and fine-grained understanding of an image's contents. Semantic segmentation is more concerned with categorising the entire scene into predefined groups rather than distinguishing between individual instances. Both tasks are important for different applications and are frequently used in tandem to extract a rich understanding of an image's contents.

Segmentaion can be carried out by using different techniques likr thresholding, region growing, edge detection, clustering, graphing methods. Lately, deep learning based image segmentation is very popular among researchers, these deep learning techniques make use of Convolutional Neural  Networks (CNN) to segment the image automatically, The scope of this project is to implement Deep Learning models, making use of CNNs to perform semantic segmentation.


### CNNs
---
Convolutional neural networks (CNNs) are a type of artificial neural network that are designed primarily for image recognition and processing. They are called "convolutional" because they process input data using a mathematical operation known as convolution.

CNNs are made up of numerous layers of linked neurons that analyse and alter incoming data via convolution, activation, pooling, and fully connected layers. The convolutional layers extract important characteristics like as edges, corners, and textures from the input data by applying a series of learnable filters. The activation layers add a nonlinear function to the convolutional layers' output, allowing the network to learn more complicated patterns in the input. The pooling layers downsample the activation layers' output, lowering dimensionality and making the network more resistant to translations in the input. The output of the pooling layers is combined into a single prediction by the fully linked layers.

CNNs are trained using a large dataset of labelled images, and the network's filters and weights are tweaked to reduce the error between predicted and true labels. A CNN, once trained, can be used to classify images, identify objects, and perform other image processing and analysis tasks. CNNs' capacity to learn from massive datasets of labelled pictures without the need for explicit feature engineering is one of its primary capabilities. As a result, they are well-suited to jobs in which the features of interest are unknown in advance, or if the features are exceedingly complicated and difficult to represent manually.


# 3.Literature Review
---

{ Eff-UNet: A novel architecture for semantic segmentation in unstructured environment } work focused on India Driving LiteDataset (IDD), which contains data from  unstructured driv-ing environment and was hosted as an online challenge inNCVPRIPG 2019. They designed Eff-UNet which combines the efficiency of a compoundscaled EfficientNet as the feature extraction encoder with a UNet decoder to reconstitute the fine-grained segmentation map. The EfficientNet retains the network's compound scalability, resulting in better performance.

{ U-Net: Convolutional Networks for Biomedical Image Segmentation}  presented a network and training strategy that relies on the strong use of data augmentation to use the available annotated samples more efficiently on the ISBI challenge for segmentation of neuronal structures in electron microscopic stacks. Segmentationof a 512x512 image takes less than a second on a recent GPU


{ Very Deep Convolutional Networks for Large-Scale Image Recognition } Tested very deep convolutional networks for large-scale image categorization (up to 19 weight layers). It was shown that representation depth improves classification accuracy and that a standard ConvNet architecture can deliver cutting-edge results on the ImageNet challenge dataset.


{ BASeg: Boundary aware semantic segmentation for autonomous driving} have put forward comparison of semantic segmentaion using differernt deep learing methods and have acheived 
mIoU of 45.76%, 81.2%, and 77.3% on ADE20K, Cityscapes, and CamVid, respectively with their BASeg noval architecture . 


{ Integrating semantic edges and segmentation information for building extraction from aerial images using UNet }combined the properties gleaned from the data at different sizes and included some additional spatial elements using the MultiRes block and their tests on roof segmentation dataset exhibited that the proposed network can improve the quantitative results of IOU to 0.78% after adding semantic edges.


{ Semantic segmentation using GSAUNet}  Gabor-based UNet (GSAUNet) model utilises the Gabor filters instead of the defualt filters in a standard UNet. they were able to produce 5.47% mean IoU and 91.44% global accuracy on the CamVid dataset. On the Cityscape dataset, the GSA UNet model achieved 92.86% pixel accuracy and 71.92% meanIoU. They have stressed on the fact that increasing the training dataset size is useful to incresase model performance














# 4. Problem Statement
---

The popularity of unmanned aerial vehicles, particularly drones, has grown over the past few years as a result of their adaptability and use. They have the the capacity to carry out jobs that would be risky or difficult for people, such as infrastructure inspection, rescue operation, televison production, advanced agriculture, delivery services and recreational use. Drones without computer vision technology will limit it's capabilities to recognise the objects, avoid obstacle and to navigate. It's possible that they won't be able to carry out duties that call for a high level of situational awareness or the capacity to adjust to dynamic environment.


# 5. Objectives
---

The objective of this project is to perform semantic segmentaion and to accurately identify, classify about 20 features namely tree, grass, vegetation, dirt, gravel, rocks, water, paved area, pool, person, dog, car, bicycle, roof, wall, fence, fence-pole, window, door, obstacle from the drone imagery.



# 6. Methodology
---

#### 6.1 Tech stack
---

Python is a popular programming language for deep learning, due to its simplicity, flexibility, and extensive libraries and frameworks. TensorFlow, Keras, PyTorch, and Theano are just a few of the deep learning modules and frameworks available in Python. These libraries include a variety of tools and utilities for developing, training, and testing deep learning models, as well as performing other tasks including data preprocessing and visualisation. It is a powerful choice for researchers and practitioners in the field, and is well-suited for a wide range of deep learning tasks and applications.

Jupyter is an open-source interactive computing application that is commonly used in deep learning. Users may create and share documents with live code, mathematics, graphics, and narrative prose. Jupyter supports python, which is the chosen programming language for this project.It is frequently used in the context of deep learning for building and testing models, as well as creating interactive notebooks that document and communicate the outcomes of deep learning experiments.

NumPy is a Python scientific computing toolkit that is commonly used in deep learning. It includes a number of Python tools and utilities for working with arrays, matrices, and numerical data. NumPy is especially beneficial for deep learning since it enables users to do quick and efficient numerical computations on huge datasets. It has support for fundamental arithmetic, linear algebra, and statistical functions, as well as a number of functions and operations for manipulating and changing arrays and matrices.

Pandas is a Python library for data manipulation and analysis that is widely used in the field of deep learning. It provides a range of tools and utilities for working with structured and tabular data in Python. Pandas is especially useful for deep learning because it enables users to effortlessly import, modify, and analyse data from a wide range of sources, including CSV files, Excel spreadsheets, and SQL databases. It offers a variety of methods and procedures for cleaning, converting, and aggregating data, as well as dealing with missing and incomplete data.It is frequently used in the context of deep learning for activities such as data preprocessing, feature engineering, and data exploration.

Matplotlib is a Python data visualisation package that is commonly used in deep learning. It includes a number of tools and utilities for making static and interactive plots and charts in Python.Matplotlib is frequently used in the context of deep learning for activities such as data exploration and visualisation, model evaluation, and result visualisation. It is also used to create data and model visualisations for publication or presentation.

OpenCV (Open Computer Vision) is a free and open-source computer vision algorithm and utility library that is widely used in image processing and computer vision. It includes a variety of tools and operations for picture acquisition, image processing, and image analysis.

Keras is an open-source software library that provides a Python interface for ANNs (artificial neural networks). It is capable of running on top of TensorFlow. Keras' flexibility to use different backends is one of its important advantages, allowing users to train their models on CPUs, GPUs, or even TPUs (tensor processing units) depending on their hardware setup. It also supports SGD (stochastic gradient descent), RMSprop, and Adam optimization methods. Keras is widely used in industry and academics for deep learning model development and training. It's especially popular for building and training convolutional neural networks (CNNs) for image classification and natural language processing.

TensorFlow is an open-source machine learning and artificial intelligence software library. Google created it and released it in 2015. TensorFlow is intended to be flexible, efficient, and portable, allowing users to execute machine learning models across multiple platforms. It has become the industry standard for building state of the art deep learning models.


### 6.2 Preprocessing the data
---
Preprocessing data for Convolutional Neural Networks (CNNs) is a critical step in the creation of a successful machine learning model. CNNs are particularly well-suited to image classification applications, and correct input data preprocessing is critical for getting decent results. Some common preprocessing steps that can be applied to image data before training a CNN are mentioned below

Labeling: 

Cropping: images that are fed to the deep learning model must be of uniform dimensions, hence It is often useful to resize the input images to a uniform size. It is important to not change the scale of the image while resizing as it alters the original information contained in the images. Images can be cropped into smaller sizes to decrease the computaion power of the training process. This is also ideal in cases where a large amount of dataset is not available.

Normalization : Normalizing the pixel values of the input images can help the CNN work better. This can be accomplished by scaling the pixel values to have a zero mean and unit variance, or by scaling the values, generally present in the range of 0-255 for RGB images to a fixed range of values like 0-1.

Data Augmentation: Data augmentation consists of creating more training examples from an existing dataset by transforming the images. This can help the CNN generalise to new data more effectively and reduce overfitting. Rotation, translation, scaling, and noise addition are all common augmentation techniques.

Balancing the Dataset: If the dataset is imbalanced (that is, there are significantly more samples of one class than the others), techniques such as undersampling or oversampling can be used to balance the distribution of classes. This can assist CNN in learning more effectively and improving overall performance.

Integer Encoding the labels : The labels of the categorical data must be converted to numbers for the computer to process, Integer encoding is a method used to represent categorical data in a numerical format. It involves assigning a unique integer to each category in the data. Integer encoding is a method for numerically representing categorical data. It entails assigning a unique integer to each data category.

One Hot Encoding: One hot encoding is a method used to represent categorical data in numerical format, especially when working with large number of categories. In one-hot encoding, each category is represented as a binary vector, with a 1 in the position corresponding to the category and 0s in all other positions. This is significant because some machine learning algorithms may make assumptions about the relationship between categories based on their ordinality that are not always correct.


#### 6.3 Train Test Split
---
We need to spilt the actual image dataset into two parts which will be seperately used to feed the deep learning model to discover and learn patterns and later on to test if the model is able to generalise the results on an unseen dataset.


### 6.4 Training models
---
UNet is one of the goto deep learning model that is used for semantic segmentation. Convolutional neural networks like U-Net were created with the goal of segmenting biomedical images. The  general description of the network consists of a contracting path called as encoder network and an expansive path called as the decoder network, which gives it the u-shaped architecture. The contracting path is a standard convolutional network that applies convolutions repeatedly, followed by rectified linear units (ReLU) and max pooling operations for each one. The objective of the decoder network is to obtain a dense classification by semantically projecting the discriminative features (lower resolution) learned by the encoder onto the pixel space (higher resolution). Upsampling, concatenation, and standard convolution operations make up the decoder. The assumption is that expanding the feature dimensions will allow us to restore the condensed feature map to its original size relative to the input image. Transposed convolution, upconvolution, and deconvolution are other names for upsampling.

Residual Neural Network, famously called as ResNet is an Artificial Neural Network that comprises of residual blocks, specifically designed to solve the vanishing gradient problem that were present in earlier deep learning networks. The VGG-19-inspired 34-layer plain network architecture used by ResNet is followed by the addition of the shortcut connection. The benefit of including this kind of skip link is that regularisation will skip any layer that degrades architecture performance. As a result, training an extremely deep neural network is possible without encountering issues with vanishing or expanding gradients. The following ResNet implementations are provided by the open-source Keras neural network library, which supports operating on top of TensorFlow and provides ResNet V1 and ResNet V2 with 50, 101, or 152 layers. ResNetV2 and the original ResNet (V1) vary primarily in that V2 applies batch normalisation before each weight layer.

Along with these two vanilla implementaions of the CNN's, we can also develop custom architectures by tweakin, gadding, removing laters. One such modification is to introduce dropout layers in the orginial architecture. 


### 6.5 Get Performance Metrics
---
It's crucial to assess a deep learning model's performance after training to see how well it generalises to unseen data. It is typical to divide the entire data into a training set, a validation set, and a test set in order to assess the performance of a deep learning model. The model is developed using the training set, tested using the validation set, and its final output is assessed using the test set. This makes it more likely that the model will be able to generalise to new data and avoid being overfit to the training set of data. It is important to generate all important metrices of performance that will be of use to validate the objective.


### 6.6 Get Activation charts
---
Activation charts are visual representations of how the input influences each neuron's output in a neural network. They aid in identifying issues like overfitting or underfitting and are utilised to see and comprehend the underlying operations of the network. They  can reveal how the network makes decisions and what attributes are most essential to it. This can help us better understand the model's behaviour and improve its performance.


### 6.7 Plot the Results
---
Plotting the results is the standard step in semantic segmentation process, here we plot the test image, the ground truth image along with the model's output for the test image side by side so that we can physically see how the model is performing.


### 6.8 Tuning the model
---
We can tune the model after post processing by adjusting the hyperparameters like architecture of the network, optimization algorithm, learning rate of the model to improve its performance.


### 6.9 Comaparsion of model performance
---
Any machine learning algorithm or model has a number of characteristics that utilise the data in various ways. The data that is provided to these algorithms is frequently altered based on the results of earlier phases of the experiment. While comparing machine learning algorithms is crucial in and of itself, there are also some less evident advantages of an effective comparision. Better performnace, Easier training, faster production are some of the major advantages of an effective comparsion. 




### 7. Conclusion
---
The synopsis report summarised the main conclusions and findings of the ongoing research literature work. It gives a comprehensive understanding of the problem statement and outlines the master's project's goal. It also gives a brief overview of the project's approach, technology stack, and applications.