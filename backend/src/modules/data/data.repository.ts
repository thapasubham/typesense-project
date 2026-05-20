import { resourceUsage } from "process";
import { typesenseClient } from "../../client/typesense.js";
import { SearchParam } from "../../types/types.js";

export class DataRepository {
  async GetData(searchParams: SearchParam) {
    console.log(searchParams);
    const client = typesenseClient.GetClient();
    let searchParameters = {
      q: searchParams.q,
      query_by: searchParams.query_by || "title,genres,tags",
      sort_by: searchParams.sort_by || "ratings_count:desc",
      filter_by: searchParams.filter_by || "ratings_count:<40 || tags:creepy",
    };
    console.log(searchParameters);
    const results = await client
      .collections("movies")
      .documents()
      .search(searchParameters);
    const transformedResults = results.hits?.map((hit) => ({
      ...hit.document,
    }));
    return transformedResults;
  }
}
