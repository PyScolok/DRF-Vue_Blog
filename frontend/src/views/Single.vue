<template>
    <div class="wrapper" id="single">
        <section class="single-blog-area">
            <div class="container">
                <div class="row">
                   <div class="col-md-12">
                        <div class="border-top">
                            <div class="col-md-8">
                                <div class="blog-area">
                                    <div class="blog-area-part">
                                        <div class="post-img">
                                            <img v-if="post.image" v-bind:src="'http://127.0.0.1:8000'+ post.image" alt="">
                                        </div>
                                        <h2>{{ post.title }}</h2>
                                        <div class="tags">
                                            <p v-for="tag in post.tags" :key="tag.id"><a href="#">{{ tag.name }}</a></p>
                                        </div>
                                        <div class="info">
                                            <h4><span>by: <span class="author-name">{{ post.author }}</span></span><span> {{ dateFormat(post.publish) }}</span> in <a class="category">{{ post.category['name'] }}</a></h4>
                                            <h4><span>update: </span><span> {{ dateFormat(post.update) }}</span></h4>
                                            <div class="feedback">
                                                <p class="feedback-item"><span><i class="fa fa-thumbs-up" aria-hidden="true"></i> {{ post.likes.length }}</span></p>
                                                <p class="feedback-item"><span><i class="fa fa-eye" aria-hidden="true"></i> {{ post.views }}</span></p>
                                                <p class="feedback-item"><span><i class="fa fa-comments" aria-hidden="true"></i> {{ post.comments.length }}</span></p>
                                            </div>
                                        </div>
                                        
                                        <div class="content" v-html="post.content"></div>
                                    </div>
                                    <Comments />
                                </div>
                            </div>
                            <Sidebar :tags="tags"/>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
    import Sidebar from '../components/sidebar'
    import Comments from '../components/comments'
    export default {
        name: "Single",
        props: ['slug'],
        data() {
           return {
               post: {},
               recentPosts: [],
               popularPosts: [],
               tags: []
           }
        },
        components: {
            Sidebar,
            Comments,

        },
        created() {
            this.loadPost();
            
        },
        methods: {
           async loadPost() {
               let rSinglePostPage = await fetch(
                    `${this.$store.getters.getServerUrl}/post/${this.slug}`
                ).then(response => response.json())
                this.post = rSinglePostPage['post'] 
                this.tags = rSinglePostPage['tags']
                console.log(rSinglePostPage)
            },
            dateFormat(value) {
                let options = {
                    year: 'numeric',
                    month: 'numeric',
                    day: 'numeric',
                    hour: 'numeric',
                    minute: 'numeric',
                }
                return new Date(value).toLocaleString("en", options);
            },
            
        },
    }
</script>
<style scoped>
    .post-img {
        margin-top: 40px;
    }

    .tags {
        display: flex;
        justify-content: left;
    }

    .category {
        color: #061e37;
        text-decoration: none;
        font-family: Geometria;
        
        font-weight: bold;
        text-transform: uppercase;
        cursor: pointer;
    }
    .info {
        position: relative;
        padding-bottom: 10px;
    }

    .info h4 {
        font-size: 12px !important;
    }

    .info::before {
        background: #e6e6e6 none repeat scroll 0 0;
        content: "";
        height: 1px;
        position: absolute;
        width: 100%;
        bottom: 0;
    }

    .feedback {
        display: flex;
        justify-content: left;
    }

    .feedback-item {
        margin-right: 10px;
    }


</style>
