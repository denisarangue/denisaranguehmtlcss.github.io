$(document).ready(function() {
  $("[data-fancybox]").fancybox({
    infobar: false,
    buttons: [
      'zoom',
      'slideShow',
      'fullScreen',
      'download',
      'thumbs'
    ],
    afterShow: function(instance, current) {
      $('<div class="fancybox-button fancybox-button--close">&#10006;</div>')
        .appendTo(current.$slide)
        .on('click', function() {
          $.fancybox.close();
        });
    }
  });
});