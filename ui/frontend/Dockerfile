FROM node:16.13.1-alpine

WORKDIR /app

ARG RVT_BACKEND

# to resolve dependencies
ENV PATH /app/node_modules/.bin:$PATH

# download all dependencies
COPY package.json ./
COPY package-lock.json ./

RUN npm ci

# copy all the source files
COPY . ./

# create an .env file with the host in it
RUN echo "REACT_APP_HOST=$RVT_BACKEND" > .env

# start the application
CMD ["npm", "start"]
