$(document).ready(function () {
  // brings user back to top
  $(".btt-link").click(function () {
    $("html, body").animate({ scrollTop: 0 }, 500);
  });

});
