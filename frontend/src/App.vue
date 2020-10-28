<template>
  <div id="app">
    <HeaderMenu />
    <router-view/>
    <FooterMenu />
  </div>
</template>

<script>
  import HeaderMenu from "./components/v-header";
  import FooterMenu from "./components/v-footer";
  export default {
    name: 'App',
    components: {
      HeaderMenu,
      FooterMenu,
    },
  }
</script>

<style>
  @import "assets/css/bootstrap.css";
  @import "assets/css/style.css";
  @import "assets/css/font-awesome.min.css";
  @import "assets/css/responsive.css";

</style>
