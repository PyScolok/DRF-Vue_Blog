<template>
  <div class="wrapper" id="comments">
    <div class="commententries">
        <h3>Comments</h3>

        <ul class="commentlist">
            <li>
                <article class="comment">
                    <header class="comment-author">
                        <img src="img/author-1.jpg" alt="">
                    </header>
                    <section class="comment-details">
                        <div class="author-name">
                            <h5><a href="#">Selina Gomez</a></h5>
                            <p>February 25 2017</p>
                        </div>
                        <div class="comment-body">
                            <p>is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard </p>
                        </div>
                        <div class="reply">
                            <p><span><a href="#"><i class="fa fa-thumbs-up" aria-hidden="true"></i></a>12</span><span><a href="#"><i class="fa fa-reply" aria-hidden="true"></i></a>7</span></p>
                        </div>
                    </section>
                </article>

                <ul class="children">
                    <li>
                        <article class="comment">
                            <header class="comment-author">
                                <img src="img/author-2.jpg" alt="">
                            </header>
                            <section class="comment-details">
                                <div class="author-name">
                                    <h5><a href="#">Khalid Hasan Zibon</a></h5>
                                    <p>February 25 2017</p>
                                </div>
                                <div class="comment-body">
                                    <p>is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard </p>
                                </div>
                                <div class="reply">
                                    <p><span><a href="#"><i class="fa fa-thumbs-up" aria-hidden="true"></i></a>12</span><span><a href="#"><i class="fa fa-reply" aria-hidden="true"></i></a>7</span></p>
                                </div>
                            </section>
                        </article>
                    </li>
                </ul>

            </li>
            <li>
                <article class="comment">
                    <header class="comment-author">
                        <img src="img/author-3.jpg" alt="">
                    </header>
                    <section class="comment-details">
                        <div class="author-name">
                            <h5><a href="#">Heath Ledger</a></h5>
                            <p>February 25 2017</p>
                        </div>
                        <div class="comment-body">
                            <p>is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard </p>
                        </div>
                        <div class="reply">
                            <p><span><a href="#"><i class="fa fa-thumbs-up" aria-hidden="true"></i></a>12</span><span><a href="#"><i class="fa fa-reply" aria-hidden="true"></i></a>7</span></p>
                        </div>
                    </section>
                </article>
            </li>
        </ul>

    </div>
    <form action="#" method="get">
        <div class="name">
            <input type="text" name="" id="" placeholder="Name" class="name">
        </div>
        <div class="email">
            <input type="email" name="" id="" placeholder="Email" class="email">
        </div>
        <div class="comment">
            <input type="text" name="" id="" placeholder="Comment" class="comment">
        </div>
        <div class="post">
            <input type="submit" value="Post">
        </div>
    </form>

  </div>
</template>

<script>
export default {
    name: 'Comments'

}
</script>

<style>

</style>