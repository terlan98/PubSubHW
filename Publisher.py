import sys, time, Constants
from os import listdir
from typing import List

try:
    import zmq
except ImportError:
    sys.stderr.write("Please install zmq (ZeroMQ) and try again\n")
    exit()


def main():
    print("Publisher started...")
    
    path = input("Folder name: ")
    directoryContents = getDirectoryContents(path)
    socket = createSocket()
    
    if not directoryContents:  # terminate if the folder is empty
        sys.stderr.write("The specified folder is empty.\n")
        exit()
    
    while True:
        print("Sending...")
        
        for content in directoryContents:
            contentString = getFormattedContentString(Constants.TOPIC, path, content)
            socket.send_string(contentString)
        
        time.sleep(Constants.SLEEP_TIME)


def createSocket() -> zmq.Socket:
    """Handles ZeroMQ publisher socket creation and binding. Returns the created socket."""
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    address = "tcp://" + Constants.PUB_HOST + ":" + Constants.PORT
    socket.bind(address)
    
    return socket


def getDirectoryContents(path: str) -> List[str]:
    """Uses the OS library to get the contents of the directory at the given path.
    Terminates the program upon failure."""
    
    try:
        directoryContents = listdir(path)  # use os library to get the contents as an array
        return directoryContents
    except:
        sys.stderr.write("Couldn't access the specified folder path. Please make sure that there are no typos and you "
                         "have the required access privileges\n")
        exit()


def getFormattedContentString(socketTopic: str, path: str, contentName: str) -> str:
    """Returns a string, appropriately formatted for describing a directory content."""
    return socketTopic + " " + path + " has " + contentName


if __name__ == "__main__":
    main()
