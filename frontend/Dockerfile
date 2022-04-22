# Stage 0, "build-stage", based on Node.js, to build and compile the frontend
FROM node:16

WORKDIR /app

COPY package.json /app/

RUN npm install

COPY ./ /app/
ARG CHOKIDAR_USEPOLLING=true
ARG FRONTEND_ENV=dev

ENV VUE_APP_ENV=${FRONTEND_ENV}
ENV CHOKIDAR_USEPOLLING=${CHOKIDAR_USEPOLLING}
ENV PORT=3000
# Comment out the next line to disable tests
# RUN npm run test:unit

# Uncomment to disable hot-reload
# RUN npm run build

RUN chown -R node /app/node_modules

USER node

CMD npm run serve
