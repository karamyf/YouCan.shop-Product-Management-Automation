
const allowedDomains = ["souqplus.com", "website1.com", "website2.com"];

$(document).ready(function() {
  // Get the current website's domain
  const currentDomain = window.location.hostname;

  if (allowedDomains.includes(currentDomain)) {
    // Add click event to the FAQ questions
    $(".faq-question").click(function() {
      var s = $(this).next(".faq-answer");
      if ($(this).hasClass("uncollapsed")) {
        s.slideUp();
        $(this).removeClass("uncollapsed");
      } else {
        $(".faq-question.uncollapsed")
          .next(".faq-answer")
          .slideUp();
        $(".faq-question.uncollapsed").removeClass("uncollapsed");
        s.slideDown();
        $(this).addClass("uncollapsed");
      }
    });
  }
});