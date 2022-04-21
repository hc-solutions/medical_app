<template>
  <ToolbarComponent :pages="pages"></ToolbarComponent>
</template>

<script>
import ToolbarComponent from "./layout/toolbar-component.vue";

export default {
  name: "App",
  components: {
    ToolbarComponent,
  },
  data() {
    return {
      pages: [],
    };
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
