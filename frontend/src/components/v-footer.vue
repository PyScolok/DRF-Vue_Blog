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
                                            <li><a href="http://localhost:8080/">Home</a></li>
                                            <li><a href="http://localhost:8080/about/">About</a></li>
                                            <li><a href="#">Contact</a></li>
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
    }
</script>

<style>
    .wrapper footer {
        margin-top: 15px;
    }
    .pages {
        float: left;
    }
    .socials {
        float: right;
    }
</style>