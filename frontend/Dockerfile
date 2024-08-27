# Base image
FROM node:22-alpine AS base

WORKDIR /app

COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

COPY . .

# Build stage
FROM base AS build

ARG HOST
ENV VITE_BACKEND_URL=${HOST}:8000

RUN yarn build

# Production stage
FROM node:22-alpine AS production

WORKDIR /app

COPY --from=build /app/build /app/build
COPY --from=base /app/package.json /app/yarn.lock ./
RUN yarn install --production --frozen-lockfile && yarn cache clean

EXPOSE 3000
CMD ["node", "build/index.js"]

# Development stage
FROM base AS development

ARG HOST
ENV VITE_BACKEND_URL=${HOST}:8000

EXPOSE 5173
CMD ["yarn", "dev"]
