import { Router, Request, Response } from "express";

const route = Router();
route.get("/", (req: Request, res: Response) => {
  res.send({ service: "Running", Health: "Ok" });
});

export const healthRouter = route;
