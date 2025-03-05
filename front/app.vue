<script setup lang="ts">
const status = ref();

const getStatus = async () => {
  const { data } = await useClient().GET("/");
  status.value = data;
};
</script>

<template>
  <v-btn class="m-6" @click="getStatus" :text="'Fetch status'" />
  <span>{{ status }}</span>
</template>
