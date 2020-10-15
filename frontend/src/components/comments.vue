<template>
  <div class="wrapper" id="comments">
    <div class="commententries">
        <h3>Comments</h3>

        <ul class="commentlist">
            <li v-for="comment in comments" :key="comment.id">
                <article class="comment">
                    <header class="comment-author">
                        <img src="img/author-1.jpg" alt="">
                    </header>
                    <section class="comment-details">
                        <div class="author-name">
                            <h5>{{ comment.author }}</h5>
                            <p>{{ comment.publish }}</p>
                        </div>
                        <div class="comment-body">
                            <p>{{ comment.text }}</p>
                        </div>
                        <div class="reply">
                            <p>
                                <span><a href="#"><i class="fa fa-reply" aria-hidden="true"></i></a></span>
                                <span v-if="comment.children">{{ comment.children.length }}</span>
                                <span v-else>0</span>
                            </p>
                        </div>
                    </section>
                </article>
                <div v-if="comment.children">
                    <ul  v-for="childComment in allCommentsRepresentation(comment.children)" :key="childComment.id" class="children">
                        <li>
                            <article class="comment">
                                <header class="comment-author">
                                    <img src="img/author-2.jpg" alt="">
                                </header>
                                <section class="comment-details">
                                    <div class="author-name">
                                        <h5>{{ childComment.author }} <span>replied to {{ childComment.parent }}</span></h5>
                                        <p>{{ childComment.publish }}</p>
                                    </div>
                                    <div class="comment-body">
                                        <p>{{ childComment.text }}</p>
                                    </div>
                                    <div class="reply">
                                        <p>
                                            <span><a href="#"><i class="fa fa-reply" aria-hidden="true"></i></a></span>
                                            <span v-if="childComment.children">{{ childComment.children.length }}</span>
                                            <span v-else>0</span>
                                        </p>
                                    </div>
                                </section>
                            </article>
                        </li>
                    </ul>
                </div>
            </li>
        </ul>

    </div>
    <form action="#" method="get">
        <div class="name">
            <input type="text" name="" id="" placeholder="Name" class="name" v-model="author">
        </div>
        <div class="comment">
            <input type="text" name="" id="" placeholder="Comment" class="comment" v-model="text">
        </div>
        <div class="post">
            <input @click="sendComment()" type="button" value="Post">
        </div>
    </form>

  </div>
</template>

<script>
export default {
    name: 'Comments',
    props: {
        comments: Array,
        postId: Number,
        
    },
    data() {
        return {
            author: '',
            text: '',
            parent: null
        }
    },
    created() {
    },
    methods:{
        allCommentsRepresentation(comments) {
            let allComments = [];
            for (let comment of comments) {
                allComments.push(comment)
                if (comment.children.length > 0) {
                    allComments = allComments.concat(this.allCommentsRepresentation(comment.children))
                }
            }
            return allComments;
        },
        async sendComment() {
            let data = {
                post: this.postId,
                author:  this.author,
                text: this.text,
                parent: this.parent,
                children: [],
            }
            fetch(`${this.$store.getters.getServerUrl}/add_comment/`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type": 'application/json',
                    },
                    body: JSON.stringify(data)
                }
            ).then(
                this.$emit('loadPost')
            )
        } 
    },
}
</script>

<style>
    .reply span {
        margin: 0 !important;
    }

    .author-name h5 {
        color: #000;
        font-family: Geometria;
        font-size: 21px;
        font-weight: 500;
        line-height: 10px;
    }

    .post input {
        
    }

</style>