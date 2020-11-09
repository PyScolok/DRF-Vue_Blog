<template>
    <div class="wrapper" id="posts">
        <section class="blog-post-area">
            <div class="container">
                <div v-if="this.masonryIsActive" v-masonry item-selector=".col-md-3" horizontal-order="true" class="row">
                    <div v-masonry-tile class="blog-post-area-style" v-for="post in posts" :key="post.id">
                        <div class="col-md-3">
                            <div class="single-post">
                                <img v-if="post.image" v-bind:src="'http://127.0.0.1:8000'+ post.image" alt="">
                                <h3><a @click="goToPost(post.slug)">{{ post.title }}</a></h3>
                                <h4><span>Posted By: <span class="author-name">{{ post.author }}</span></span></h4>
                                <span v-html="post.content"></span>
                                <span><a  @click="goToPost(post.slug)" class="post-button">Read more...</a></span>
                                <h4><span>{{ post.publish }}</span></h4>
                            </div>
                        </div>
                    </div>
                </div>
                <div v-else  class="row">
                    <div class="blog-post-area-style" v-for="post in posts" :key="post.id">
                        <div class="col-md-3">
                            <div class="single-post">
                                <img v-if="post.image" v-bind:src="'http://127.0.0.1:8000'+ post.image" alt="">
                                <h3><a  @click="goToPost(post.slug)">{{ post.title }}</a></h3>
                                <h4><span>Posted By: <span class="author-name">{{ post.author }}</span></span></h4>
                                <span v-html="post.content"></span>
                                <span><a  @click="goToPost(post.slug)" class="post-button">Read more...</a></span>
                                <h4><span>{{ post.publish }}</span></h4>
                            </div>
                        </div>
                    </div>
                </div>
                <button class="addPosts" @click="loadAdditionalPosts">More posts</button>
            </div>
        </section>
    </div>
</template>

<script>
    export default {
        name: "PostsList",
        data() {
            return {
                posts: [],
                newposts: [],
                masonryIsActive: false,
            }
        },
        created() {
            this.activateMasonry();
            this.loadListPosts();
            window.addEventListener('resize', this.activateMasonry);
        },
        destroyed() {
            window.removeEventListener('resize', this.activateMasonry);
        },
        methods: {
            async loadListPosts() {
                let listPosts = await fetch(
                    `${this.$store.getters.getServerUrl}/main`
                ).then(response => response.json());
                this.posts = listPosts["posts"];
            },
            async loadAdditionalPosts() {
                let adPosts = await fetch(
                    `${this.$store.getters.getServerUrl}/main?count=${this.posts.length}`
                ).then(response => response.json());
                this.newposts = adPosts['posts'];
                this.posts = this.posts.concat(this.newposts);
            },
            activateMasonry() {
                if (window.innerWidth >= 992 && !this.masonryIsActive) {
                    this.masonryIsActive = true;
                } else if (window.innerWidth < 992 && this.masonryIsActive) {
                    this.masonryIsActive = false;
                }
            },
            goToPost(slug) {
                this.$router.push({name: 'Single', params: {slug: slug}})
            }
        }
    }
</script>

<style>
    .single-post p {
        max-height: 228px;
        overflow: hidden;
    }

    .single-post a {
        cursor: pointer;
    }

    .single-post img {
        margin-bottom: 25px;
    }

    .post-button {
        color: #061e37;
        text-decoration: none;
        font-family: Geometria;
        font-size: 15px;
        font-weight: bold;
        cursor: pointer;
    }

    .addPosts {
        position: relative;
        display: block;
        background: #40c4ff;
        color: #fff;
        font-family: "Raleway", sans-serif;
        font-size: 15px;
        font-weight: 600;
        margin: 0 auto;
        padding: 26px 50px;
        border: none;
        text-transform: uppercase;
        outline: none;
        
    }
</style>