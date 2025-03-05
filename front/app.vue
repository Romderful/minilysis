<script setup lang="ts">
const status = ref();

const getStatus = async () => {
  const { data } = await useClient().GET("/");
  status.value = data;
};
</script>

<template>
  <v-btn @click="getStatus" :text="'Fetch status'" />
  <span>{{ status }}</span>
</template>
