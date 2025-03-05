<script setup lang="ts">
import createClient from "openapi-fetch";
import type { paths } from "./schema";

const client = createClient<paths>({ baseUrl: "http://localhost:8000" });

const status = ref();
const err = ref();

const call = async () => {
  const { data, error } = await client.GET("/");
  status.value = data;
  err.value = error;
};
</script>

<template>
  <div>
    <button @click="call" />
  </div>
  <div>
    <span v-if="status">{{ status }}</span>
    <span v-else>{{ err }}</span>
  </div>
</template>
