<template>
  <div id="app">
    <AppToolbar :pages="pages"></AppToolbar>
  </div>
</template>

<script>
import AppToolbar from "./layout/app-toolbar.vue";

export default {
  name: "App",
  components: {
    AppToolbar,
  },
  data() {
    return {
      pages: [{ en: "Doctors" }, { en: "Analyses" }, { en: "Reminder" }],
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
