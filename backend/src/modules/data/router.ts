import { Router, Request, Response } from "express";
import { DataController } from "./data.controller.js";

const route = Router();
const dataController = new DataController();
route.get("/", dataController.GetData);

export const dataRouter = route;
