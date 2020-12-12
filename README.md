# INFT 3507 – Assignment 2 (Publish/Subscribe)
This python program uses the [ZeroMQ](https://github.com/zeromq/pyzmq) library for implementing the publisher/subscriber messaging model.

## ⚡️ How can I run it?
 1. Open 2 terminals
 2. Run `python3 Publisher.py` in the **first** terminal
 3. Provide a folder path for the Publisher. 
> *Note: Some OSs, like MacOS, may not allow access to specific folders (like Desktop) by default. If an error occurs due to this reason, please try another folder or change your OS settings to allow access. Alternatively, you can try running the program with 'sudo'*

Publisher will periodically *(every 10 seconds, by default)* publish the contents of the given folder.

 6. Run `python3 Subscriber.py` in the **second** terminal
 7. The subscriber will print the messages that it receives.

## ⚠️ Warning
* You should use Python 3
* You should have ZeroMQ installed on your system
