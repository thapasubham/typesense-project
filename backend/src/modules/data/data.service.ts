import { SearchParam } from "../../types/types.js";
import { DataRepository } from "./data.repository.js";

export class DataService {
  private dataRepo: DataRepository;
  constructor(dataRepository: DataRepository) {
    this.dataRepo = dataRepository;
  }
  async GetData(searchParam: SearchParam) {
    return await this.dataRepo.GetData(searchParam);
  }
}
