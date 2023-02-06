import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

iris = load_iris()
iris_X, iris_y = iris.data[:-1,:], iris.target[:-1]
iris_y= pd.get_dummies(iris_y).values
trainX, testX, trainY, testY = train_test_split(iris_X, iris_y, test_size=0.33, random_state=42)

numFeatures = trainX.shape[1]
numLabels = trainY.shape[1]

trainX = tf.constant(trainX, dtype='float32')
trainY = tf.constant(trainY, dtype='float32')
testX = tf.constant(testX, dtype='float32')
testY = tf.constant(testY, dtype='float32')

W = tf.Variable(tf.zeros([4, 3]))
b = tf.Variable(tf.zeros([3]))

weights = tf.Variable(tf.random.normal([numFeatures,numLabels], mean=0., stddev=0.01, name="weights"),dtype='float32')

bias = tf.Variable(tf.random.normal([1,numLabels], mean=0., stddev=0.01, name="bias"))

def logistic_regression(x):
    apply_weights_OP = tf.matmul(x, weights, name="apply_weights")
    add_bias_OP = tf.add(apply_weights_OP, bias, name="add_bias") 
    activation_OP = tf.nn.sigmoid(add_bias_OP, name="activation")
    return activation_OP

Epochs = 700

learningRate = tf.optimizers.schedules.ExponentialDecay(initial_learning_rate=0.0008, decay_steps=trainX.shape[0], decay_rate= 0.95, staircase=True)

loss_object = tf.losses.MeanSquaredLogarithmicError()
optimizer = tf.optimizers.SGD(learningRate)

#metric
def accuracy(y_pred, y_true):

    correct_prediction = tf.equal(tf.argmax(y_pred, 1), tf.argmax(y_true, 1))

    return tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

def run_optimization(x, y):
    with tf.GradientTape() as g:
        pred = logistic_regression(x)
        loss = loss_object(pred, y)
    gradients = g.gradient(loss, [weights, bias])
    optimizer.apply_gradients(zip(gradients, [weights, bias]))
    
display_step = 10
epoch_values = []
accuracy_values = []
loss_values = []
loss = 0
diff = 1
# Training epochs
for i in range(Epochs):
    if i > 1 and diff < .0001:
        print("change in loss %g; convergence."%diff)
        break
    else:
        run_optimization(trainX, trainY)
        
        if i % display_step == 0:
            epoch_values.append(i)
            
            pred = logistic_regression(testX)

            newLoss = loss_object(pred, testY)

            loss_values.append(newLoss)
            
            acc = accuracy(pred, testY)
            accuracy_values.append(acc)
            
            diff = abs(newLoss - loss)
            loss = newLoss

            print("step %d, training accuracy %g, loss %g, change in loss %g"%(i, acc, newLoss, diff))

print("final accuracy on test set: %s" %acc.numpy())

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.plot(loss_values)
plt.show()