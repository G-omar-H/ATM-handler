#!/bin/bash

# Define image name
IMAGE_NAME="atm_handler"

# Build the Docker image
docker build -t $IMAGE_NAME .

# Start the container in detached mode
docker run -d \
  --network host \
  --name atm_handler_container \
  $IMAGE_NAME

# Print confirmation message
echo "ATM data seeder deployed successfully."
