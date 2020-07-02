const databaseInit = (env) => {
  if (!env("DATABASE") || env("DATABASE") !== "postgres") {
    console.log("DATABASE in .env not found/equal to 'postgres'. Using SQLite");
    return {
      client: "sqlite",
      filename: env("DATABASE_FILENAME", ".tmp/data.db"),
    };
  }

  console.log("Using postgres");
  return {
    client: env("DATABASE"),
    host: env("DATABASE_HOST"),
    port: env.int("DATABASE_PORT"),
    database: env("DATABASE_NAME"),
    username: env("DATABASE_USERNAME"),
    password: env("DATABASE_PASSWORD"),
    ssl: env.bool("DATABASE_SSL", false),
  };
};

module.exports = ({ env }) => ({
  defaultConnection: "default",
  connections: {
    default: {
      connector: "bookshelf",
      settings: databaseInit(env),
      options: {},
    },
  },
});
