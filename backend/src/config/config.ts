export const config = {
  TYPESENSE_HOST: process.env.TYPESENSE_HOST || "localhost",
  TYPESENSE_PORT: parseInt(process.env.TYPESENSE_PORT || "8108"),
  TYPESENSE_PROTOCOL: process.env.TYPESENSE_PROTOCOL || "http",
  TYPESENSE_API_KEY: process.env.TYPESENSE_API_KEY || "xyz",
};
