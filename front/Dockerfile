FROM node:23.9.0-alpine

WORKDIR /app

RUN corepack enable pnpm

COPY package.json .

ENTRYPOINT ["sh", "./dev-entrypoint.sh"]
