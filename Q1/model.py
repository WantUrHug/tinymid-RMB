import tensorflow as tf

#build model
def inference(inputs, num_classes):

	outputs = tf.layers.Conv2D(filters = 32, kernel_size = (3,3), strides = (1,1), activation = "relu", padding = "SAME")(inputs)

	outputs = tf.layers.MaxPooling2D(pool_size = (2,2), strides = (2,2))(outputs)
	
	outputs = tf.layers.Conv2D(filters = 64, kernel_size = (3,3), strides = (1,1), activation = "relu", padding = "SAME")(outputs)
	
	outputs = tf.layers.MaxPooling2D(pool_size = (2,2), strides = (2,2))(outputs)
	
	outputs = tf.layers.Flatten()(outputs)

	outputs = tf.layers.Dense(512, activation = "relu")(outputs)
	outputs = tf.layers.Dense(256, activation = "relu")(outputs)
	outputs = tf.layers.Dense(num_classes, activation = "relu")(outputs)

	return outputs

def loss(logits, labels):

	softmax = tf.nn.softmax_cross_entropy_with_logits(logits = logits, labels = labels)
	return tf.reduce_mean(softmax)

def train(loss, lr):
	return tf.train.GradientDescentOptimizer(lr).minimize(loss)

def evaluation(logits, labels):
	return tf.reduce_mean(tf.cast(tf.equal(tf.argmax(logits, 1), tf.argmax(labels, 1)), tf.float32))