import * as fs from "fs/promises";
import { typesenseClient } from "../client/typesense.js";
import { createCollection } from "../modules/data/data.types.js";

async function seedData() {
  try {
    const moviesInJsonl = await fs.readFile("./temp/books.jsonl", "utf-8");

    const client = typesenseClient.GetClient();

    console.log("Starting data import...");

    const returnData = await client
      .collections("movies")
      .documents()
      .import(moviesInJsonl, { action: "upsert" });

    console.log("Import completed successfully!");
    console.log(returnData);
  } catch (error) {
    console.error("Error seeding data:", error);
  }
}

async function runSetup() {
  try {
    await createCollection();

    await seedData();
  } catch (error) {
    console.error("Setup failed midway:", error);
  }
}

runSetup();
