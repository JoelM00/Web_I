var testemunhasHTML = '';
        
for (var i = 0; i < testemunhas.length; i++) {
    var testemunha = testemunhas[i];
    var html =  '<div class="swiper-slide box-testemunha">'+
                    '<div class="testemunha-imagem">'+
                        '<img src="'+testemunha.imagem+'">'+
                    '</div>'+
                    '<span class="testemunha-nome">'+testemunha.nome+'</span>'+
                    '<span class="testemunha-profissao">CEO, '+testemunha.empresa+'</span>'+
                    '<p class="testemunha-texto">'+testemunha.texto+'</p>'+
                '</div>';

    testemunhasHTML += html;
}

document.getElementById("testemunhas-box").innerHTML = testemunhasHTML;

var postsHTML = '';
        
for (var i = 0; i < 5; i++) {
    var post = posts[i];
    var html = '<div class="swiper-slide">'+
                '<div class="post-box">'+
                    '<div class="post-wrapper">'+
                        '<a href="news-detail.html?id='+(i+1)+'" class="post-link">'+
                            '<div class="post-imagem">'+
                                '<img src="'+post.imagem+'" class="img-responsive">'+
                            '</div>'+
                            '<span class="post-title">'+post.titulo+'</span>'+
                            '<p class="post-subtitle">By <strong class="bold">'+post.autor+'</strong> | '+post.data+'</p>'+
                        '</a>'+
                    '</div>'+
                '</div>'+
            '</div>';

    postsHTML += html;
}

document.getElementById("posts-slider").innerHTML = postsHTML;


var mySwiper = new Swiper('.swiper-container-testemunhas', {
    pagination: {
        el: ".swiper-pagination-testemunhas",
        clickable: true,
    },
});

var mySwiperPosts = new Swiper('.swiper-container-posts ', {
    slidesPerView: 3,
    spaceBetween: 30,
    pagination: {
        el: '.swiper-pagination-posts',
        clickable: true,
    },
    breakpoints: {
        320: {
            slidesPerView: 1,
            spaceBetween: 20
        },
        768: {
            slidesPerView: 2,
            spaceBetween: 30
        },
        980: {
            slidesPerView: 3,
            spaceBetween: 30
        }
    }
});