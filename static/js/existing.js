$('.switch').on('click', function(e) {
      $('.existing').toggleClass("existing-show"); //you can list several class names 
      e.preventDefault();
    });