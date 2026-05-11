import Typesense from "typesense";
import { config } from "../config/config.js";

class TypesenseClient {
  private client: Typesense.Client;

  constructor() {
    this.client = new Typesense.Client({
      nodes: [
        {
          host: config.TYPESENSE_HOST,
          port: config.TYPESENSE_PORT,
          protocol: config.TYPESENSE_PROTOCOL,
        },
      ],
      apiKey: config.TYPESENSE_API_KEY,
      connectionTimeoutSeconds: 2,
    });
  }

  GetClient() {
    return this.client;
  }
}

export const typesenseClient = new TypesenseClient();
