import { Router } from "express";
import { healthRouter } from "./health/healthRoute.js";
import { dataRouter } from "./data/router.js";

const router = Router();
router.use("/health", healthRouter);
router.use("/dataset", dataRouter);
export const routes = router;
