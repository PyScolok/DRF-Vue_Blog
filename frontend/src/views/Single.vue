<template>
    <div class="single">
        <SinglePost post='post' />
    </div>
</template>

<script>
    import SinglePost from '../components/single'
    export default {
        name: "Single",
        props: ['slug'],
        data() {
           return {
               post: {}
           }
        },
        components: {
            SinglePost,

        },
        created() {
            this.loadPost();
            
        },
        methods: {
           async loadPost() {
               this.post = await fetch(
                   `${this.$store.getters.getServerUrl}/post/${this.slug}`
               ).then(response => response.json())
               console.log(this.post)
               console.log(this.slug)
            },
        },
    }
</script>