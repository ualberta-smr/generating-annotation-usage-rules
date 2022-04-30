FROM node:16.13.1-alpine

WORKDIR /app

RUN npm i -g markserv

# copy all the source files
COPY . ./

# start the application
CMD ["markserv", "-p", "8000", "-a", "0.0.0.0", "README.md"]