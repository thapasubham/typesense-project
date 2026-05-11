import { Request, Response } from "express";

export class DataController {
  GetData(req: Request, res: Response) {
    res.send({ service: "sigma", Health: "Ok" });
  }
}
