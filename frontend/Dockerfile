# Use the official Node.js image as the base image
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json (or yarn.lock) files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the React app
RUN npm run build

# Set the environment to production
ENV NODE_ENV=production

# Expose the port the app will run on
EXPOSE 3000

# Start the app
CMD ["npm", "start"]