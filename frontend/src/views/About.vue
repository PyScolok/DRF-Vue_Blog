<template>
    <div class="wrapper" id="about">
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <h2>About</h2>
                    <p>
                        <span class="drop_caps">L</span>orem ipsum dolor sit amet consectetur adipisicing elit.
                        Laudantium cumque nam perferendis cupiditate et repellendus itaque ipsam? Ipsam officia quia
                        necessitatibus dolor nostrum, quo, voluptate enim libero esse ullam consequuntur. Lorem,
                        ipsum dolor. Lorem ipsum dolor sit amet consectetur adipisicing elit. Ad eligendi cumque 
                        ducimus, hic nihil animi fugit earum eius autem exercitationem omnis doloribus libero 
                        iusto error quos asperiores sint id!
                    </p>
                    <p>    
                        <span class="drop_caps">L</span>orem ipsum dolor sit amet consectetur adipisicing elit.
                        Laudantium cumque nam perferendis cupiditate et repellendus itaque ipsam? Ipsam officia quia
                        necessitatibus dolor nostrum, quo, voluptate enim libero esse ullam consequuntur. Lorem,
                        ipsum dolor. Lorem ipsum dolor sit amet consectetur adipisicing elit. Ad eligendi cumque 
                        ducimus, hic nihil animi fugit earum eius autem exercitationem omnis doloribus libero 
                        iusto error quos asperiores sint id!
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
    .drop_caps {
        color: #40c4ff;
        float: left;
        font-family: Geometria;
        font-size: 60px;
        font-weight: 400;
        margin: 18px 30px 20px 20px;
        position: relative;
    }

    .drop_caps::after {
        color: rgb(64, 196, 255);
        content: "”";
        font-size: 40px;
        right: -15px;
        position: absolute;
        top: -7px;
        font-weight: 500;
    }
    .drop_caps::before {
        color: rgb(64, 196, 255);
        content: "”";
        font-size: 40px;
        left: -20px;
        position: absolute;
        top: -7px;
        font-weight: 500;
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