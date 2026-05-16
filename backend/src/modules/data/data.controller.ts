import { Request, Response } from "express";
import { DataService } from "./data.service.js";
import { SearchParam } from "../../types/types.js";

export class DataController {
  private dataService: DataService;
  constructor(dataService: DataService) {
    this.dataService = dataService;
  }
  async GetData(req: Request, res: Response) {
    const serach: SearchParam = req.query;
    const result = await this.dataService.GetData(serach);
    res.status(200).send(result);
  }
}
