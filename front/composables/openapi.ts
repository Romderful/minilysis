export const useClient = () => {
  const nuxtApp = useNuxtApp();
  return nuxtApp.$openapi;
};
