import { typesenseClient } from "../../client/typesense.js";
import { SearchParam } from "../../types/types.js";

export class DataRepository {
  async GetData(searchParams: SearchParam) {
    const client = typesenseClient.GetClient();
    let searchParameters = {
      q: "experyment",
      query_by: "title",
      facet_by: "publication_year",
      sort_by: "average_rating:desc",
    };

    const results = await client
      .collections("books")
      .documents()
      .search(searchParams);

    return results;
  }
}
