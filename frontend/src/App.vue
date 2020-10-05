<template>
  <div id="app">
    <Header :categories="categories"/>
    <router-view/>
    <Footer />
  </div>
</template>

<script>
  import Header from "./components/header";
  import Footer from "./components/footer";
  export default {
    name: 'App',
    data() {
      return {
        categories: [],
      }
    },
    components: {
      Header,
      Footer,
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
