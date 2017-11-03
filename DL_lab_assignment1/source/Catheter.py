""" Simple linear regression example in TensorFlow
This program tries to predict the number of thefts from
the number of fire in the city of Chicago
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import xlrd

DATA_FILE = 'data/x02.xlsx'

# Step 1: read in data from the .xls file
book = xlrd.open_workbook(DATA_FILE, encoding_override="utf-8")
sheet = book.sheet_by_index(0)
data = np.asarray([sheet.row_values(i) for i in range(1, sheet.nrows)])
n_samples = sheet.nrows - 1

# Step 2: create placeholders for input X (number of fire) and label Y (number of theft)
X1 = tf.placeholder(tf.float32, name='weight')
X2 = tf.placeholder(tf.float32, name='height')
Y = tf.placeholder(tf.float32, name='catheter_length')

# Step 3: create height and weight initialized to 0
h = tf.Variable(0.0, name='height')
w = tf.Variable(0.0, name='weight')

# Step 4: build model to predict Y
Y_predicted = X1 * h + X2 * w

# Step 5: use the square error as the loss function
loss = tf.square(Y - Y_predicted, name='loss')

# Step 6: using gradient descent with learning rate of 0.0000001 to minimize loss
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0000001).minimize(loss)

with tf.Session() as sess:
    # Step 7: initialize the necessary variables, in this case, w1, w2 and b
    sess.run(tf.global_variables_initializer())

    writer = tf.summary.FileWriter('./graphs/linear_reg', sess.graph)

    # Step 8: train the model
    for i in range(12):  # train the model 50 epochs
        total_loss = 0
        for x1, x2, y in data:
            # Session runs train_op and fetch values of loss
            _, l = sess.run([optimizer, loss], feed_dict={X1: x1, X2: x2, Y: y})
            total_loss += l
        print('Epoch {0}: {1}'.format(i, total_loss / n_samples))

    # close the writer when you're done using it
    writer.close()

    # Step 9: output the values of w and b
    w1,w2= sess.run([h, w])

# plot the results
X1, X2, Y = data.T[0], data.T[1], data.T[2],
plt.plot(X1, X2, Y, 'bo', label='Real data')
plt.plot(X1, X2, X1 * w1 + X2 * w2, 'r', label='Predicted data')
plt.legend()
plt.show()