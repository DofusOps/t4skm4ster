# Base image
FROM python:latest

# Set working directory
WORKDIR /taskmaster

# Copy requirements
COPY ./taskmaster/requirements.txt /taskmaster

# Install requirements
RUN apt update && \
    apt install nginx -y && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Run bash
CMD ["bash"]