<template>
  <div class="wrapper" id="sidebar">
        <div class="col-md-4">
            <div class="button-group filters-button-group">
                <button class="button is-checked">Recent</button>
                <button class="button">popular</button>
            </div>
            <div class="grid">
                <div class="portfolio-item recent">
                    <img src="img/portfolio1.jpg" alt="">
                    <div class="portfolio-text">
                        <h5><a href="#">Pay Close Attention To People Who Don’t Clap When You Win recent1.</a></h5> 
                        <p>By Kabbo Liate <span>|</span>25 February 2017</p>
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
    props: ['tags', ],
    data() {
        return {

        }
    },
    created() {
        console.log(this.tags)

    },
    methods: {

    }

}
</script>

<style>

</style>