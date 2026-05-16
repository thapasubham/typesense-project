import { Router, Request, Response } from "express";
import { DataController } from "./data.controller.js";
import { DataService } from "./data.service.js";
import { DataRepository } from "./data.repository.js";

const route = Router();
const dataService = new DataService(new DataRepository());
const dataController = new DataController(dataService);
route.get("/", dataController.GetData.bind(dataController));
export const dataRouter = route;
