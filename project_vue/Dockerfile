# Use official Node.js runtime as a parent image
FROM node:14

# Set work directory
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy project
COPY . .

# Expose port
EXPOSE 8080

# Command to run the application
CMD ["npm", "run", "serve"]