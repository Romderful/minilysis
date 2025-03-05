<script setup lang="ts">
import createClient from "openapi-fetch";
import type { paths } from "./schema";

const client = createClient<paths>({ baseUrl: "http://localhost:8000" });

const status = ref();

const getStatus = async () => {
  const { data } = await client.GET("/");
  status.value = data;
};
</script>

<template>
  <div>
    <button @click="getStatus" />
  </div>
  <div>
    <span>{{ status }}</span>
  </div>
</template>
