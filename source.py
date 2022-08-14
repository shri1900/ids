import socket     # Import socket module
import time
import pandas as pd

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 8000                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
test_data= pd.read_csv("test_data.csv")
s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
print ('Got connection from', addr)
idx = 0
while True:
    print(" ".join(test_data.iloc[idx].values.astype("str")))
    c.send(bytes(" ".join(test_data.iloc[idx].values.astype("str")),encoding='utf8'))
    idx+=1
    if idx == len(test_data):
        idx = 0
    print("SENT")
    time.sleep(10)