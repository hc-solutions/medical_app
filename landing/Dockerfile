FROM node:16 as build-stage

ARG FRONTEND_ENV=production
ENV VUE_APP_ENV=${FRONTEND_ENV}
ENV VUE_APP_NAME=${VUE_APP_NAME}

WORKDIR /app

COPY ./package*.json /app/
# COPY ./yarn.lock /app/

RUN npm install

COPY ./ /app/

RUN npm run build

FROM nginx:1.15 as production-stage

COPY --from=build-stage /app/dist/ /usr/share/nginx/html
COPY --from=build-stage /app/nginx.conf /etc/nginx/conf.d/default.conf
COPY ./nginx-backend-not-found.conf /etc/nginx/extra-conf.d/backend-not-found.conf

WORKDIR /usr/share/nginx/html
