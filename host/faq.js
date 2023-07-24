  $(document).ready(function() {
    // List of allowed website domains
    const allowedDomains = ["souqplus.youcan.shop", "website1.com", "website2.com"];

    // Get the current website's domain
    const currentDomain = window.location.hostname;

    if (allowedDomains.includes(currentDomain)) {
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
