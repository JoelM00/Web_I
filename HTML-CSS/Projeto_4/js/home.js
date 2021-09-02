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