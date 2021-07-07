// CREDITS: https://css-tricks.com/value-bubbles-for-range-inputs/
//
var rangeSlider = function () {
    var slider = $('.range-slider'),
        range = $('.range-slider__range'),
        value = $('.range-slider__value');

    slider.each(function () {

        value.each(function () {
            var value = $(this).prev().attr('value');
            $(this).html(value);
        });

        range.on('input', function () {
            $(this).next(value).html(this.value);
        });
    });
};

rangeSlider();

$('.toast').toast('show');

$('[data-toggle="tooltip"]').tooltip();

// document.querySelectorAll('[data-toggle=collapse]').forEach((el) => {
//     el.addEventListener('click', () => {
//         // const collapse = el.closest('.row').querySelector('.collapse');
//         // const caret = el.closest('.row').querySelector('.caret-container').querySelector('i.fas');
//         // if (collapse.classList.contains('show')) {
//         //     console.log('show');
//         //     caret.classList.remove('fa-caret-down');
//         //     caret.classList.add('fa-caret-right');
//         // } else {
//         //     console.log('hide');
//         //     caret.classList.add('fa-caret-down');
//         //     caret.classList.remove('fa-caret-right');
//         // }

//     })
// });


$('.review-collapse').on('show.bs.collapse', function () {
    var label_elem = document.getElementById($(this).attr('aria-labelledby')).querySelector('.review-caret');
    $(label_elem).css({ 'transform': 'rotate(90deg)' });
    // $(label_elem).toggleClass('fa-angle-right');
    // $(label_elem).toggleClass('fa-angle-down');
});

$('.review-collapse').on('hide.bs.collapse', function () {
    var label_elem = document.getElementById($(this).attr('aria-labelledby')).querySelector('.review-caret');
    $(label_elem).css({ 'transform': 'rotate(0deg)' })
});