FROM node:latest

WORKDIR /src

COPY package-lock.json .
COPY . .

RUN npm install

RUN npm install react-scripts --save

RUN npm i react-bootstrap

RUN npm i react-router-dom react-router-bootstrap

EXPOSE 3000

CMD ["npm", "start"]