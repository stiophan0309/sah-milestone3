  $( document ).ready(function() {
    $('.read-more').click(function(){
        $(this).parent().toggleClass('expanded');
    });
});