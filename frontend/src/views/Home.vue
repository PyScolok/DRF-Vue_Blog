<template>
    <div class="home">
        <Banner />
        <Posts />
    </div>
</template>

<script>
    import Banner from "../components/banner";
    import Posts from "../components/posts";
    export default {
        name: "Home",
        components: {
            Banner,
            Posts,
        },
        created() {

        },
        methods: {

        },
    }
</script>
