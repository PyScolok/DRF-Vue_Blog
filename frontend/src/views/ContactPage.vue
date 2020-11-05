<template>
    <div class="wrapper" id="contact">
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <h2>Contacts</h2>
                    <p>
                        E-mail: blog@example.com
                    </p>
                    <p>
                        <a href="https://vk.com/blog">VK</a> 
                    </p>
                    <p>
                        <a href="https://www.instagram.com/nik_rod96/">Instagram</a> 
                    </p>
                </div>
            </div>
        </div>        
    </div>
</template>

<script>
    export default {
        name: "AboutPage",
    }
</script>
    

<style>
    #contact {
       flex-grow: 1;
    }

    p {
        font-family: Geometria;
        font-size: 15px;
        font-weight: 500;
        line-height: 35px;
        position: relative;
        text-align: justify;
    }

    h2 {
        text-align: center;
        color: #010101;
        font-family: Geometria;
        font-size: 38px;
        font-weight: 500;
        margin-bottom: 60px;
        margin-top: 45px;
    }
</style>