$(document).ready(function() {

    var $window = $(window),
        $nav = $('.navbar'),
        $footnotes = $('.footnote');

    function init() {
        fixFootnotes();
        $window.on('load hashchange', fixHashOffset);
    }

    function fixFootnotes() {
        $footnotes.each(function(i, el) {
            $el = $(el);
            $el.appendTo($el.closest('article'));
        });
    }

    function fixHashOffset() {
        if($window.scrollTop() >= $nav.offset().top) {
            scrollBy(0, -$nav.height());
        }
    }

    init();
});
