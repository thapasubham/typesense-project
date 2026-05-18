import { CollectionSchema } from "typesense/lib/Typesense/Collection.js";
import { typesenseClient } from "../../client/typesense.js";

export const moviesSchema = {
  name: "movies",
  fields: [
    { name: "title", type: "string" },
    { name: "genres", type: "string[]", facet: true },
    { name: "tags", type: "string[]", facet: true },
    { name: "average_rating", type: "float" },
    { name: "ratings_count", type: "int32", facet: true },
  ],
  default_sorting_field: "ratings_count",
} as const;

export async function createCollection() {
  const client = typesenseClient.GetClient();
  try {
    console.log("Creating 'movies' collection...");
    const data = await client
      .collections()
      .create(moviesSchema as unknown as CollectionSchema);
    console.log("Collection created successfully:", data.name);
    return data;
  } catch (error) {
    console.error("Error creating collection:", error);
    throw error;
  }
}
