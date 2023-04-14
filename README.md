# Bird Call Recognition Service

This repository contains the code for a bird call recognition service. The service consists of a server (cloud) API that uses a bird call recognition model and a Raspberry Pi client that listens to audio input and sends the data to the server for recognition.

## Repository Structure

The repository is organized into two main folders: `server` and `client`.

- `server`: Contains the code for the server API, including the bird call recognition model and audio processing utilities.
- `client`: Contains the code for the Raspberry Pi client, which listens to audio input and communicates with the server API.

## Installation and Setup

### Server

1. Make sure you have Python 3.8 or higher and Docker installed.
2. Navigate to the `server` folder.
3. Install the required Python packages:

`pip install -r requirements.txt`
4. Build the Docker image:

`docker build -t bird-call-recognition-server .`

5. Run the Docker container:

`docker run -p 8000:8000 bird-call-recognition-server`


### Client

1. Set up your Raspberry Pi with a compatible microphone.
2. Navigate to the `client` folder.
3. Give execute permissions to the `setup.sh` script:

   ```bash
   chmod +x setup.sh
   ```
4. Run the setup.sh script to install Python, required packages, and any additional dependencies:
`./setup.sh`
5. Modify the config.py file to point to your server's IP address and port.
6. Run the client application:
`python3 main.py`

## Usage

When the client is running on the Raspberry Pi, it will continuously listen to audio input, send it to the server for recognition, and process the results.

## Contributing

Please submit issues and pull requests for bug fixes, new features, or other improvements.
