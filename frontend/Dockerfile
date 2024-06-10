# Use the official Node.js image from the Docker Hub
FROM node:18.17.0

# Create a directory for the app
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json /app/
RUN npm install

# Copy the project files
COPY . /app/

# Expose the port
EXPOSE 3000

# Start the application
CMD ["npm", "run", "dev"]
