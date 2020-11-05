<template>
    <div class="wrapper" id="footer">
        <footer class="footer">
            <div class="container">
                <div class="row">
                    <div class="col-md-12">
                        <div class="footer-bg">
                            <div class="row">
                                <div class="pages">
                                    <div class="footer-menu">
                                        <ul>
                                            <li><a @click="goTo('HomePage')">Home</a></li>
                                            <li><a @click="goTo('AboutPage')">About</a></li>
                                            <li><a @click="goTo('ContactPage')">Contact</a></li>
                                        </ul>
                                    </div>
                                </div>
                                <div class="socials">
                                    <div class="footer-icon">
                                        <p>
                                            <a href="https://vk.com/nrgizerbot"><i class="fa fa-vk" aria-hidden="true"></i></a>
                                            <a href="https://github.com/PyScolok"><i class="fa fa-github" aria-hidden="true"></i></a>
                                            <a href="https://www.instagram.com/nik_rod96/"><i class="fa fa-instagram" aria-hidden="true"></i></a>
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
    </div>
</template>

<script>
    export default {
        name: "FooterMenu",
        methods: {
            goTo(name) {
                this.$router.push({name: name})
            }
        }
    }
</script>

<style>
    a {
        cursor: pointer;
    }
    .wrapper footer {
        margin-top: 15px;
        flex-grow: 0;
    }
    .pages {
        float: left;
    }
    .socials {
        float: right;
    }
</style>