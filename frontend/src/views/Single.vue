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
                                        <div v-if="loading" class="info">
                                            <h4><span>by: <span class="author-name">{{ post.author }}</span></span><span> {{ post.publish }}</span> in <a class="category">{{ post.category.name }}</a></h4>
                                            <h4><span>update: </span><span> {{ post.update }}</span></h4>
                                            <div class="feedback">
                                                <p class="feedback-item"><span><i class="fa fa-thumbs-up" aria-hidden="true"></i> {{ post.likes.length }}</span></p>
                                                <p class="feedback-item"><span><i class="fa fa-eye" aria-hidden="true"></i> {{ post.views }}</span></p>
                                                <p class="feedback-item"><span><i class="fa fa-comments" aria-hidden="true"></i> {{ getCommentsCount(post.comments) }}</span></p>
                                            </div>
                                        </div>
                                        
                                        <div class="content" v-html="post.content"></div>
                                    </div>
                                    <Comments :comments="post.comments" />
                                </div>
                            </div>
                            <Sidebar @loadPost='changePostData' :tags="tags" :recentPosts="recentPosts" :popularPosts="popularPosts"/>
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
               tags: [],
               loading: false,
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
                ).then(response => response.json());
                this.post = rSinglePostPage['post'];
                this.tags = rSinglePostPage['tags'];
                this.recentPosts = rSinglePostPage['recent_posts'];
                this.popularPosts = rSinglePostPage['popular_posts'];
                this.loading = true;
                console.log(this.post)
            },
            changePostData(data) {
                this.post = data['post']
            },
            getCommentsCount(comments) {
                let commentsCount = 0;
                for (let comment of comments) {
                    commentsCount ++
                    if (comment.children.length > 0) {
                        commentsCount += this.getCommentsCount(comment.children)
                    }
                }
                return commentsCount;
            }
            
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

    .author-name {
        font-weight: bold;
    }

    .feedback {
        display: flex;
        justify-content: left;
    }

    .feedback-item {
        margin-right: 10px;
    }


</style>
