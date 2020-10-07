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
                        <h5><a @click="goTo(post.slug)">{{ post.title }}</a></h5> 
                        <p>By {{ post.author }} <span>|</span>{{ dateFormat(post.publish) }}</p>
                    </div>
                </div>
            </div>
            <div v-if="popularList" class="grid">
                <div v-for="post in popularPosts" :key="post.id" class="portfolio-item recent">
                    <img v-if="post.image" v-bind:src="'http://127.0.0.1:8000'+ post.image" alt="">
                    <img v-else src="http://placehold.it/72x72/33bee5/ffffff/&text=NOPHOTO"/>
                    <div class="portfolio-text">
                        <h5><a @click="goTo(post.slug)">{{ post.title }}</a></h5> 
                        <p>By {{ post.author }} <span> | <i class="fa fa-eye" aria-hidden="true"></i> {{ post.views }}</span></p>
                    </div>
                </div>
            </div>
            <div class="tags">
                <h2 class="sidebar-title">Tags</h2>
                <p v-for="tag in tags" :key="tag.id"><a href="#">{{ tag.name }}</a></p>
            </div>
            <div class="newsletter">
                <h2 class="sidebar-title">Subscribe To oUR nEWSLETTER</h2>
                <form action="#" method="post">
                    <input type="email" name="" id="" placeholder="Email">
                    <input type="submit" value="Subscribe">
                </form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Sidebar',
    props: ['tags', 'recentPosts', 'popularPosts'],
    data() {
        return {
            recentList: true,
            popularList: false,

        }
    },
    created() {
        

    },
    methods: {
        goTo(slug) {
            this.$router.push({name: 'Single', params: {slug: slug}})
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
        recentListActivate() {
            this.recentList  = !this.recentList;
            this.popularList = !this.popularList;
        },
        popularListActivate() {
            this.recentList  = !this.recentList;
            this.popularList = !this.popularList;
        },

    }

}
</script>

<style>
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