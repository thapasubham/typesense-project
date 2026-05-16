import { CollectionSchema } from "typesense/lib/Typesense/Collection.js";
import { typesenseClient } from "../../client/typesense.js";

export const booksSchema = {
  name: "books",
  fields: [
    { name: "title", type: "string" },
    { name: "authors", type: "string[]", facet: true },
    { name: "publication_year", type: "int32", facet: true },
    { name: "ratings_count", type: "int32" },
    { name: "average_rating", type: "float" },
  ],
  default_sorting_field: "ratings_count",
} as const;

export async function createCollection() {
  const client = typesenseClient.GetClient();
  try {
    console.log("Creating 'books' collection...");
    const data = await client
      .collections()
      .create(booksSchema as unknown as CollectionSchema);
    console.log("Collection created successfully:", data.name);
    return data;
  } catch (error) {
    console.error("Error creating collection:", error);
    throw error;
  }
}
