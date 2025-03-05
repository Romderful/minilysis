<script setup lang="ts">
const status = ref();

const getStatus = async () => {
  const { data } = await useClient().GET("/");
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
