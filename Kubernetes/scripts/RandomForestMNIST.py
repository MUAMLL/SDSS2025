from torchvision.datasets import MNIST
from skimage.feature import hog
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from tqdm import tqdm
import numpy as np
import os

NUM_TREES = int(os.environ.get("SK_NUM_TREES", "3"))
NUM_JOBS = int(os.environ.get("SK_NUM_JOBS", "1"))

print(f"Running random forest with {NUM_TREES} trees and {NUM_JOBS} jobs")

######
# Download MNIST
######
train_dataset = MNIST(download=True, root="~/data", train=True)
test_dataset = MNIST(download=True, root="~/data", train=False)

##### 
# Generate Train Features
#####
print("Generating Train Features")
train_features = np.empty((len(train_dataset), 108))
train_labels = np.empty(len(train_dataset), np.int32)
for i, (img, label) in tqdm(enumerate(train_dataset), ncols=80, total=len(train_dataset)):
    train_features[i] = hog(np.asarray(img), orientations=12, cells_per_block=(3,3))
    train_labels[i] = label

#####
# Generate Test Features
#####
print("Generating Test Features")
test_features = np.empty((len(test_dataset), 108))
test_labels = np.empty(len(test_dataset), np.int32)
for i, (img, label) in tqdm(enumerate(test_dataset), ncols=80, total=len(test_dataset)):
    test_features[i] = hog(np.asarray(img), orientations=12, cells_per_block=(3,3))
    test_labels[i] = label

######
# Train Model
#######
print("Training the model")
model = RandomForestClassifier(n_estimators=NUM_TREES, n_jobs=NUM_JOBS, verbose=1)
model.fit(train_features, train_labels)

####
# Score Model
#####
print("Evaluating the model")
model_accuracy = model.score(test_features, test_labels)
print(f"Model Accuracy = {model_accuracy*100:.2f}%")