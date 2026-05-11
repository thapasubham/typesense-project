import express from "express";
import { routes } from "./modules/router.js";
async function startServer() {
  const port = 5000;
  const app = express();

  app.use("/", routes);
  app.listen(port, () => {
    console.log(`listening at port localhost:${port}`);
  });
}
startServer();
