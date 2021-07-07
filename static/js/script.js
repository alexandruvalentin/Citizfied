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

$('.review-collapse').on('show.bs.collapse', function () {
    var label_elem = document.getElementById($(this).attr('aria-labelledby')).querySelector('.review-caret');
    $(label_elem).css({ 'transform': 'rotate(90deg)' });
});

$('.review-collapse').on('hide.bs.collapse', function () {
    var label_elem = document.getElementById($(this).attr('aria-labelledby')).querySelector('.review-caret');
    $(label_elem).css({ 'transform': 'rotate(0deg)' })
});