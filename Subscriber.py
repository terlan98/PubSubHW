import zmq, Constants


def main():
	print("Subscriber started...")
	socket = createSocket()
	
	while True:
		content = socket.recv()
		print(content.decode("utf-8"))


def createSocket() -> zmq.Socket:
	"""Handles ZeroMQ subscriber socket creation and binding. Returns the created socket."""
	context = zmq.Context()
	socket = context.socket(zmq.SUB)
	address = "tcp://" + Constants.SUB_HOST + ":" + Constants.PORT
	
	socket.connect(address)
	socket.subscribe(Constants.TOPIC)
	socket.subscribe(Constants.SEPARATOR_TOPIC)
	
	return socket


if __name__ == "__main__":
	main()
