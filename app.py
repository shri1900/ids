from flask import Flask, render_template      
import socket               # Import socket module
import tensorflow as tf
import numpy as np

#physical_devices = tf.config.list_physical_devices('GPU')
#tf.config.experimental.set_memory_growth(physical_devices[0], True)

app = Flask(__name__)

@app.route("/")
def home():
    temp = s.recv(1024).decode(encoding='utf-8')
    print(temp)
    temp_arr = np.array(list(map(float,temp.split()))).reshape((-1,1,40))
    print(temp_arr)
    prediction = np.argmax(model.predict(temp_arr)[0])
    class_predicted = classes[prediction]
    s.send(bytes("1",encoding='utf8'))
    attack = class_predicted.upper()
    action = actionInfo[class_predicted]

    return render_template('index.html',attack=attack,action=action)

    
if __name__ == "__main__":
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 8000                # Reserve a port for your service.
    model = tf.keras.models.load_model("classifier")
    classes = ['dos', 'normal', 'probe']
    actionInfo = {
        'dos': 'DoS Attack Found...Reconfiguring the Routers and Alert Generated to Admin',
        'normal': 'Network Packet is Safe, Access Granted for Cloud Services',
        'probe': 'Probe Attack Found, Blocking the Source IP'
    }

    s.connect((host, port))
    app.run(debug=True,use_reloader=False)
