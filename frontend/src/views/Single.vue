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
                                            <p v-for="tag in post.tags" :key="tag.id"><a @click="goToTag(tag.slug)">{{ tag.name }}</a></p>
                                        </div>
                                        <div v-if="loading" class="info">
                                            <h4><span>by: <span class="author-name">{{ post.author }}</span></span><span> {{ post.publish }}</span> in <a class="category">{{ post.category.name }}</a></h4>
                                            <h4><span>update: </span><span> {{ post.update }}</span></h4>
                                            <div class="feedback">
                                                <p class="feedback-item"><span><i class="fa fa-thumbs-up" aria-hidden="true"></i> {{ getLikesCount(post.activity) }}</span></p>
                                                <p class="feedback-item"><span><i class="fa fa-eye" aria-hidden="true"></i> {{ post.activity.length }}</span></p>
                                                <p class="feedback-item"><span><i class="fa fa-comments" aria-hidden="true"></i> {{ getCommentsCount(post.comments) }}</span></p>
                                            </div>
                                        </div>
                                        <div class="content" v-html="post.content"></div>
                                    </div>
                                    <p>
                                        <span><button class="like_dislike" @click="sendActivity(true)"><i class="fa fa-thumbs-up" aria-hidden="true"></i></button></span>
                                        <span><button class="like_dislike" @click="sendActivity()"><i class="fa fa-thumbs-down" aria-hidden="true"></i></button></span>
                                    </p>
                                    <CommentsList @loadPost='loadPost' :comments="post.comments" :postId="post.id" />
                                </div>
                            </div>
                            <SidebarMenu @loadPost='changePostData' :tags="tags" :recentPosts="recentPosts" :popularPosts="popularPosts"/>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
    import SidebarMenu from '../components/v-sidebar'
    import CommentsList from '../components/v-comments'
    export default {
        name: "Single",
        props: ['slug'],
        data() {
           return {
               postSlug: this.slug,
               post: {},
               recentPosts: [],
               popularPosts: [],
               tags: [],
               loading: false,
               like: false,
           }
        },
        components: {
            SidebarMenu,
            CommentsList,
        },
        created() {
            this.loadPost();
        },
        beforeRouteUpdate (to, from, next) {
            this.postSlug = to.params.slug;
            this.loadPost();
            next();
        },
        methods: {
           async loadPost() {
               let singlePostPage = await fetch(
                    `${this.$store.getters.getServerUrl}/post/${this.postSlug}`
                ).then(response => response.json());
                this.post = singlePostPage['post'];
                this.tags = singlePostPage['tags'];
                this.recentPosts = singlePostPage['recent_posts'];
                this.popularPosts = singlePostPage['popular_posts'];
                this.loading = true;
                this.sendActivity()
            },
            async sendActivity(like=null) {
                let data = {
                    post: this.post.id,
                    like: like,
                }
                fetch(`${this.$store.getters.getServerUrl}/add_view/`,
                    {
                        method: "POST",
                        headers: {
                            "Content-Type": 'application/json',
                        },
                        body: JSON.stringify(data)
                    }
                );
            },
            changePostData(data) {
                this.postSlug = data['slug'];
                this.loadPost();
            },
            getCommentsCount(comments) {
                let commentsCount = 0;
                for (let comment of comments) {
                    commentsCount ++;
                    if (comment.children.length > 0) {
                        commentsCount += this.getCommentsCount(comment.children);
                    }
                }
                return commentsCount;
            },
            getLikesCount(post) {
                const result = post.filter(act => act.like);
                return result.length;
            },
            goToTag(slug) {
                this.$router.push({name: 'PostsByTag', params: {slug: slug}})
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
    
    .like_dislike {
        border: medium none;
        border-radius: 0;
        color: #000;
        display: inline-block;
        font-family: Geometria;
        font-size: 20px;
        font-weight: 500;
        padding: 21px;
        text-transform: uppercase;
        width: 50%;
        outline: none;
    }

    .like_dislike.is-checked {
        background: #40c4ff;
        color: #fff;
    }
    .like_dislike:hover {
        background: #40c4ff;
        color: #fff;
    }
</style>
