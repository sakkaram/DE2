import pulsar

# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://localhost:6650')

# Subscribe to a topic and subscription
consumer = client.subscribe('DEtop', subscription_name='DE-sub')
numWords = 4
i = 0
mlist = []
flag = True
while flag is True:
    i += 1
    msg = consumer.receive()
    CapText = msg.data().decode().upper()
    mlist.append(CapText)
    if i == numWords:
        flag = False
        message = ' '.join(mlist)
        try:
            print("Received message : '%s'" % message)
            consumer.acknowledge(msg)
        except:
            consumer.negative_acknowledge(msg)
# Destroy pulsar client
client.close()

