# FIRST STEP
FROM node:20-alpine AS builder

WORKDIR /app

# we need to copy paquets config files
COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

# SECOND STEP
FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

# to sumarize what just happened :
# - step 1 -> converts all the frontend code framework into understandable scripts for the browser
# - step 2 -> just copy these files inside the new container that will allow nginx to run and communicate with our backend