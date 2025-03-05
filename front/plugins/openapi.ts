import createClient from "openapi-fetch";
import type { paths } from "@/schema";

export default defineNuxtPlugin(() => {
  const openapi = createClient<paths>({
    baseUrl: "http://localhost:8000",
  });

  return {
    provide: {
      openapi,
    },
  };
});
