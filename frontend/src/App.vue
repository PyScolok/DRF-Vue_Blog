<template>
  <div id="app">
    <HeaderMenu :categories="categories"/>
    <router-view/>
    <FooterMenu />
  </div>
</template>

<script>
  import HeaderMenu from "./components/v-header";
  import FooterMenu from "./components/v-footer";
  export default {
    name: 'App',
    data() {
      return {
        categories: [],
      }
    },
    components: {
      HeaderMenu,
      FooterMenu,
    },
    created() {
      this.loadListCategories()
    },
    methods: {
      async loadListCategories() {
        let listCategories = await fetch(
          `${this.$store.getters.getServerUrl}/categories`
        ).then(response => response.json())
        this.categories = listCategories["categories"]
      }
    }
  }
</script>

<style>
  @import "assets/css/bootstrap.css";
  @import "assets/css/style.css";
  @import "assets/css/font-awesome.min.css";
  @import "assets/css/responsive.css";
</style>
