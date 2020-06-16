# Douglas API

## How to start


```
npm i
touch .env
```

In the `.env` file, enter:

```
DATABASE_HOST=your_postgres_db_host
DATABASE_PORT=usually_this_is_5432
DATABASE_NAME=your_postgres_db_name
DATABASE_USERNAME=your_postgres_user
DATABASE_PASSWORD=your_postgres_pw
```

Enter `strapi develop`, and it should automatically load your `.env` files as Strapi launches. This will launch the Strapi admin in development mode. You are free to edit content types and plugins in this mode.

To run Strapi in production mode, run the server.js file. For this, a process manager, such as PM2, is recommended. You can simply run it like `NODE_ENV=production pm2 start server.js --node-args="-r dotenv/config" --name="douglas-api"`. This will cause Strapi to run in production mode with the environment variables loaded.

## Hosting

We need to use NGINX to host this. The best way is to set up NGINX virtual hosts. We simply need to make all requests to example.domain.com point to our server IP address, and have NGINX capture and redirect that request to port 1337 (or whatever port Strapi runs on).

## Contribution

Just make pull requests. The core team will review it and let you know what happens.
