import socket               # Import socket module
import tensorflow as tf
import numpy as np

#physical_devices = tf.config.list_physical_devices('GPU')
#tf.config.experimental.set_memory_growth(physical_devices[0], True)

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 8000                # Reserve a port for your service.
model = tf.keras.models.load_model("classifier")
classes = ['dos', 'normal', 'probe']
s.connect((host, port))
while True :
    temp = s.recv(1024).decode()
    temp_arr = np.array(list(map(float,temp.split()))).reshape((-1,1,40))
    prediction = np.argmax(model.predict(temp_arr)[0])
    class_predicted = classes[prediction]
    print("Attack Type : {}".format(class_predicted))
