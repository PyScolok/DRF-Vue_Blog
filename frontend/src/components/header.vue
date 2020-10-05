<template>
    <div class="wrapper" id="header">
        <header class="header">
            <div class="container">
                <div class="row header-menu">
                    <div class="col-md-2">
                        <div class="logo">
                            <h2>Blog</h2>
                        </div>
                    </div>
                    <div class="col-md-10">
                        <div class="menu">
                            <div class="nav">
                                <a class="nav-item" href="">Home</a>
                                <a class="nav-item" href="">Categories ▼
                                    <div class="dropdown">
                                        <a v-for="category in categories" :key="category.id" class="nav-item last" href="">{{ category.name }}</a>
                                    </div>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </header>
    </div>
</template>

<script>
    export default {
        name: "Header",
        props: ['categories'],

    }   
</script>

<style scoped>
    .header-menu {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .nav {
        display: flex;
        justify-content: flex-end;
        flex-wrap: nowrap;  
    }

    .nav-item {
        position: relative;
        display: inline-block;
        list-style: outside none none;
        color: rgb(6, 30, 55);
        font-family: "Raleway", sans-serif;
        font-size: 15px;
        font-weight: 600;
        padding: 26px 50px;
        text-decoration: none;
        text-transform: uppercase;
    }

    .last {
        width: 100%;
        margin: 4px 0;
    }

    .dropdown {
        width: inherit;
        background: #fff;
        visibility: hidden;
        opacity: 0;
        position: absolute;
        transition: all 0.5s ease;
        left: 0;
        top: 100%;
        display: none;
        z-index: 1;
    }

    .nav-item:hover > .dropdown,
    .dropdown:hover {
        visibility: visible;
        opacity: 1;
        display: block;
    }

    .nav-item:hover {
        background: #40c4ff;
        color: #fff;
    }
</style>