// CREDITS: https://css-tricks.com/value-bubbles-for-range-inputs/
//
var rangeSlider = function () {
    var range = $('.range-slider__range'),
        value = $('.range-slider__value'),
        stars = $('.stars-container');

    value.each(function () {
        var value = $(range).attr('value');
        var width = 100 / 5 * value;
        $(this).html(value);
        $(stars).width(width + '%');
    });

    range.on('input', function () {
        var width = 100 / 5 * this.value;
        $(value).html(this.value);
        $(stars).width(width + '%');
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

$('.delete').confirm({
    title: "Are you sure?",
    content: 'Please confirm...',
    buttons: {
        delete: {
            text: 'Delete',
            btnClass: 'btn-danger',
            action: function () {
                location.href = this.$target.attr('href');
            }
        },
        close: {
            btnClass: 'btn-info'
        }
    }
});
