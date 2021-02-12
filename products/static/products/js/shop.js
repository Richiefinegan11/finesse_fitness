$(document).ready(function () {
  // brings user back to top
  $(".btt-link").click(function () {
    $("html, body").animate({ scrollTop: 0 }, 500);
  });

  // // // Hides the sorting icon links
  // $("#sort-container").hide();
  // // Makes the sorting icon links visable/hidden when trigger is clicked
  // $("#sort-trigger").click(function () {
  //   if ($("sort-container:visible").length)
  //     $("#sort-container").hide("slide", { direction: "right" }, 1000);
  //   else $("#sort-container").show("slide", { direction: "right" }, 1000);
  // });
});
