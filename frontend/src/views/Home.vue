<template>
    <div class="home">
        <HomeBanner />
        <PostsList />
    </div>
</template>

<script>
    import HomeBanner from "../components/v-banner";
    import PostsList from "../components/v-posts";
    export default {
        name: "Home",
        components: {
            HomeBanner,
            PostsList,
        },
    }
</script>
