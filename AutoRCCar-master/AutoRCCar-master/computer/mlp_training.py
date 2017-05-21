

import cv2
import numpy as np
import glob

print 'Loading training data...'
e0 = cv2.getTickCount()

# load training data
image_array = np.zeros((1, 38400))
label_array = np.zeros((1, 4), 'float')
training_data = glob.glob('training_data/*.npz')

for single_npz in training_data:
    with np.load(single_npz) as data:
        print data.files
        train_temp = data['train']
        train_labels_temp = data['train_labels']
        print train_temp.shape ## prints matrix form in brackets(a,b)
        print train_labels_temp.shape ## (prints in matrix form in brackets (a,b)
    image_array = np.vstack((image_array, train_temp)) # stacks empty array with frame array
    label_array = np.vstack((label_array, train_labels_temp)) #stacks empty label image_array with frame array

train = image_array[1:, :] # removes first array it was first vstacked with
train_labels = label_array[1:, :] # removes the empty array it was first vstacked with
print train.shape
print train_labels.shape

e00 = cv2.getTickCount() # returns num of clock cycles to stack each array
time0 = (e00 - e0)/ cv2.getTickFrequency() # calculates taken to stack each total arrays
print 'Loading image duration:', time0

# set start time
e1 = cv2.getTickCount() # start another timer

# create MLP
layer_sizes = np.int32([38400, 32, 4]) # define layer size of NN
model = cv2.ANN_MLP() # use built in library for NN
model.create(layer_sizes)
#define our hyper parameters
criteria = (cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS, 500, 0.0001)# train with 500 interations and error rate 0.0001
criteria2 = (cv2.TERM_CRITERIA_COUNT, 100, 0.001)# train with 100 interations, error rate of 0.001
params = dict(term_crit = criteria,
               train_method = cv2.ANN_MLP_TRAIN_PARAMS_BACKPROP, # method of training back prop
               bp_dw_scale = 0.001,
               bp_moment_scale = 0.0 )
#cv2.ANN_MLP.train(inputs, outputs, sampleWeights[, sampleIdx[, params[, flags]]])
print 'Training Neural Network   ...'
num_iter = model.train(train, train_labels, None, params = params)

# set end time
e2 = cv2.getTickCount()
time = (e2 - e1)/cv2.getTickFrequency()
print 'Training duration:', time

# save param
model.save('mlp_xml/mlp.xml')

print 'Ran for %d iterations' % num_iter

#reshape results into understandable format?
ret, resp = model.predict(train)
prediction = resp.argmax(-1)
print 'Prediction:', prediction
true_labels = train_labels.argmax(-1)
print 'True labels:', true_labels

print 'Testing...'
train_rate = np.mean(prediction == true_labels)# mean of the training label and
print 'Train rate: %f:' % (train_rate*100) # convert train rate to percentage.