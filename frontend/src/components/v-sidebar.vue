<template>
  <div class="wrapper" id="sidebar">
        <div class="col-md-4">
            <div class="button-group filters-button-group">
                <button @click="recentListActivate()" v-bind:class="{ 'is-checked': recentList }" class="button">Recent</button>
                <button @click="popularListActivate()" v-bind:class="{ 'is-checked': popularList }" class="button">popular</button>
            </div>
            <div v-if="recentList" class="grid">
                <div v-for="post in recentPosts" :key="post.id" class="portfolio-item recent">
                    <img v-if="post.image" v-bind:src="'http://127.0.0.1:8000'+ post.image" alt="">
                    <img v-else src="http://placehold.it/72x72/33bee5/ffffff/&text=NOPHOTO"/>
                    <div class="portfolio-text">
                        <h5><a @click="goToPost(post.slug)">{{ post.title }}</a></h5> 
                        <p>By {{ post.author }} <span>|</span>{{ post.publish }}</p>
                    </div>
                </div>
            </div>
            <div v-if="popularList" class="grid">
                <div v-for="post in popularPosts" :key="post.id" class="portfolio-item recent">
                    <img v-if="post.image" v-bind:src="'http://127.0.0.1:8000'+ post.image" alt="">
                    <img v-else src="http://placehold.it/72x72/33bee5/ffffff/&text=NOPHOTO"/>
                    <div class="portfolio-text">
                        <h5><a @click="goToPost(post.slug)">{{ post.title }}</a></h5> 
                        <p>By {{ post.author }} <span> | <i class="fa fa-eye" aria-hidden="true"></i> {{ post.activity.length }}</span></p>
                    </div>
                </div>
            </div>
            <div class="tags">
                <h2 class="sidebar-title">Tags</h2>
                <p v-for="tag in tags" :key="tag.id"><a @click="goToTag(tag.slug)">{{ tag.name }}</a></p>
            </div>
            <div class="newsletter">
                <h2 class="sidebar-title">Subscribe To oUR nEWSLETTER</h2>
                <form action="#" method="post">
                    <input type="email" name="" id="" placeholder="Email" v-model="email">
                    <input @click="subscribe(); clearForm()" type="button" value="Subscribe">
                </form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SidebarMenu',
    props: ['tags', 'recentPosts', 'popularPosts'],
    data() {
        return {
            recentList: true,
            popularList: false,
            post: {},
            email: '',
        }
    },
    methods: {
        goToPost(slug) {
            this.$router.push({name: 'Single', params: {slug: slug}})
            this.$emit('loadPost', {slug: slug})
        },
        goToTag(slug) {
            this.$router.push({name: 'PostsByTag', params: {slug: slug}})
        },
        recentListActivate() {
            this.recentList  = !this.recentList;
            this.popularList = !this.popularList;
        },
        popularListActivate() {
            this.recentList  = !this.recentList;
            this.popularList = !this.popularList;
        },
        async subscribe() {
            let data = {
                email: this.email,
            }
            fetch(`${this.$store.getters.getServerUrl}/add_subscriber/`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type": 'application/json',
                    },
                    body: JSON.stringify(data)
                }
            );
        },
        clearForm() {
            this.email = '';
        }, 
    }
}
</script>

<style>
    .wrapper a {
        cursor: pointer;
    }

    .button-group button {
        outline: none;
    }

    .portfolio-text h5 {
        cursor: pointer;
    }

    i {
        margin-left: 10px;
    }
</style>