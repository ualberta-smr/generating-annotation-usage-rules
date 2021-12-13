FROM node:16.13.1-alpine

WORKDIR /app

# to resolve dependencies
ENV PATH /app/node_modules/.bin:$PATH

# download all dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm ci

# copy all the source files
COPY . ./

# start the application
CMD ["npm", "start"]
