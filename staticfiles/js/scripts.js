$(".phone__mask").mask("+7 (999) 999 - 99 - 99");

(function () {
    'use strict'
    var forms = document.querySelectorAll('.needs-validation')

    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }

                form.classList.add('was-validated')
            }, false)
        })
})()


$(document).ready(function () {
    var owl = $('.slider');
    owl.owlCarousel({
        margin: 0,
        nav: true,
        dots: true,
        autoHeight: true,
        loop: true,
        items: 1
    });
})


$(document).ready(function () {
    var owl = $('.carousel__1');
    owl.owlCarousel({
        nav: true,
        dots: true,
        autoHeight: true,
        loop: true,
        responsive: {
            0: {
                items: 2,
                margin: 12,
            },
            576: {
                items: 2,
                margin: 12,
            },
            768: {
                items: 3,
                margin: 24,
            },
            1200: {
                items: 4,
                margin: 24,
            }
        }
    });
})


$(document).ready(function () {
    var owl = $('.carousel__2');
    owl.owlCarousel({
        nav: true,
        dots: true,
        autoHeight: true,
        loop: true,
        responsive: {
            0: {
                items: 1.2,
                margin: 0,
            },
            576: {
                items: 1.2,
                margin: 0,
            },
            768: {
                items: 3,
                margin: 24,
            },
            1200: {
                items: 4,
                margin: 24,
            }
        }
    });
})


$(document).ready(function () {
    $("a.topLink").click(function () {
        $("html, body").animate({
            scrollTop: $($(this).attr("href")).offset().top + "px"
        }, {
            duration: 0,
            easing: "swing"
        });
        return false;
    });
});


$(function () {
    $(window).scroll(function () {
        var top = $(document).scrollTop();
        if (top > 40) $('.head').addClass('head_fixed');
        else $('.head').removeClass('head_fixed');
    });
});


$(function () {
    AOS.init({
        duration: 1500,
        offset: 0,
        once: false
    });
});

(function () {
    // Элементы
    const progressBar = document.getElementById('progressBar');
    const indicator = document.getElementById('scrollIndicator');

    // Флаг для оптимизации (чтобы не обновлять лишний раз)
    let ticking = false;

    // Функция обновления прогресса
    function updateProgress() {
        // Высота всего документа с учётом прокрутки
        const scrollTop = window.scrollY || document.documentElement.scrollTop || 0;
        // Полная высота страницы (включая прокручиваемую часть)
        const scrollHeight = document.documentElement.scrollHeight;
        // Высота видимой области окна
        const clientHeight = document.documentElement.clientHeight;

        // Максимально возможная прокрутка
        const maxScroll = scrollHeight - clientHeight;

        // Если страница не прокручивается или вмещается в экран — 0%
        let percent = 0;
        if (maxScroll > 0) {
            percent = (scrollTop / maxScroll) * 100;
            // Ограничим от 0 до 100 (на случай дробей)
            percent = Math.min(100, Math.max(0, percent));
        }

        // Применяем ширину
        progressBar.style.width = percent + '%';
    }

    // Обработчик события scroll с использованием requestAnimationFrame
    function onScroll() {
        if (!ticking) {
            window.requestAnimationFrame(function () {
                updateProgress();
                ticking = false;
            });
            ticking = true;
        }
    }

    // Подписываемся на событие прокрутки
    window.addEventListener('scroll', onScroll, { passive: true });

    // Также обновляем при изменении размера окна (чтобы пересчитать проценты)
    window.addEventListener('resize', function () {
        // при ресайзе обновляем сразу (без rAF, чтобы не накапливать)
        updateProgress();
    }, { passive: true });

    // Вызываем один раз при загрузке, чтобы установить начальное состояние (0%)
    updateProgress();

    // (Опционально) если контент подгружается динамически — можно вызывать updateProgress()
    console.log('✅ Индикатор прокрутки активен');
})();