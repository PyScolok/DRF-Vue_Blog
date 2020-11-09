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
                                        <span><button class="like_dislike" v-bind:class="{ 'is-checked': userLikedThis }" @click="sendActivity(!userLikedThis)"><i class="fa fa-thumbs-up" aria-hidden="true"></i></button></span>
                                    </p>
                                    <CommentsList @loadPost='loadPost' :comments="post.comments" :postId="post.id" :postSlug="post.slug"/>
                                </div>
                            </div>
                            <SidebarMenu :tags="tags" :recentPosts="recentPosts" :popularPosts="popularPosts"/>
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
               clientIp:'',
               userLikedThis: false,
               postSlug: this.slug,
               post: {},
               postId: 0,
               recentPosts: [],
               popularPosts: [],
               tags: [],
               loading: false,
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
        watch: {
            postId() {
                this.sendActivity()
            },
        },
        methods: {
           async loadPost() {
               let singlePostPage = await fetch(
                    `${this.$store.getters.getServerUrl}/post/${this.postSlug}`
                ).then(response => response.json());
                this.clientIp = singlePostPage['ip'];
                this.post = singlePostPage['post'];
                this.postId = singlePostPage['post']['id'];
                this.tags = singlePostPage['tags'];
                this.recentPosts = singlePostPage['recentPosts'];
                this.popularPosts = singlePostPage['popularPosts'];
                this.loading = true;
                if (this.post.activity.find(this.isUserLiked)) {
                   this.userLikedThis = true;
                }
                else {
                    this.userLikedThis = false;
                }
            },
            async sendActivity(like=null) {
                let data = {
                    post: this.post.id,
                }
                if (!(like === null)) {
                    data.like = like;
                }
                fetch(`${this.$store.getters.getServerUrl}/post/${this.postSlug}/add_view/`,
                    {
                        method: "POST",
                        headers: {
                            "Content-Type": 'application/json',
                        },
                        body: JSON.stringify(data)
                    }
                );
                if (!(like === null)) {
                    this.loadPost();
                }
            },
            isUserLiked(element) {
                if(element.ip === this.clientIp && element.like){
                    return true
                }
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
    #single {
       flex-grow: 1;
    }

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
        width: 100%;
        outline: none;
    }

    .is-checked {
        background: #40c4ff;
        color: #fff;
    }
</style>
