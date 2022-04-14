import pulsar

# Input String
INPUT_STRING = 'this is my message'
#starting the client
client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('DEtop')
try:
    strArray = INPUT_STRING.split(' ', 1)
    Current = strArray[0]
    Next = strArray[1]
except:
    Current = INPUT_STRING
    Next = None
    producer.send(Current.encode('utf-8'))
while Next is not None:
    producer.send(Current.encode('utf-8'))
    strArray = []
    try:
        strArray = Next.split(' ', 1)
        Current = strArray[0]
        Next = strArray[1]
    except:
        Current = Next
        Next = None
        producer.send(Current.encode('utf-8'))
client.close()
