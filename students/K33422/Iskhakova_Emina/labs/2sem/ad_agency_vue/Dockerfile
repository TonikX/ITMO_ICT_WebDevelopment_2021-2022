FROM node:12

RUN mkdir /front
WORKDIR /front
COPY package*.json ./

RUN npm install
RUN npm install -g @vue/cli
COPY . .

CMD ["npm", "run", "serve"]

