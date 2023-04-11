#!/bin/bash

# Build image
docker build -t dockmaster .

# Run image
docker run -it -v ./taskmaster:/taskmaster dockmaster