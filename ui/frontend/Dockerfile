FROM node:16.13.1-alpine

WORKDIR /app

ARG RVT_BACKEND
ARG RVT_TUTORIAL

# to resolve dependencies
ENV PATH /app/node_modules/.bin:$PATH

# download all dependencies
COPY package.json ./
COPY package-lock.json ./

RUN npm ci && npm install -g serve

# copy all the source files
COPY . ./

# create an .env file with the hosts in it
RUN echo "REACT_APP_HOST=$RVT_BACKEND" > .env
RUN echo "REACT_APP_TUTORIAL_URL=$RVT_TUTORIAL" >> .env

RUN npm run build

# start the application
CMD ["serve", "-s", "build", "-l", "80"]
