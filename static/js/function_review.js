// This is not working in the external js file,
// So i have added this code in the internal js that is in the header.html file !

// ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// --------------------------------- ho gaya solve ! -------------------------
// ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

// This is a Review Script and is not working in the external js.
// so, i have added this code to the internal script
$(document).ready(function () {
  console.log("Review Form is running Safly ! ");

  const monthNames = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jly",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
  ];

  $("#commentForm").submit(function (e) {
    e.preventDefault(); // Prevent the default form submission behavior

    let dt = new Date();
    let time =
      dt.getDay() +
      " " +
      monthNames[dt.getUTCMonth()] +
      ", " +
      dt.getFullYear();

    $.ajax({
      data: $(this).serialize(),
      method: $(this).attr("method"),
      url: $(this).attr("action"),
      dataType: "json",
      success: function (res) {
        console.log("Comment Saved to DB ..... ");

        if (res.bool == true) {
          $("#review-res").html(
            " Your Review has been Added Successfully ! Thank you for your Review :) "
          );
          $(".hide-comment-form").hide();
          $(".hide-it").hide();

          let _html = '<div class="swiper-slide slide">';
          _html += "<h4>Reviewed On : " + time + "</h4>";
          _html += '<div class="stars">';
          /*
              _html +=   '<i class="fas fa-star"></i>'
              _html +=   '<i class="fas fa-star"></i>'
              _html +=   '<i class="fas fa-star"></i>'
              _html +=   '<i class="fas fa-star"></i>'
              _html +=   '<i class="fas fa-star"></i>'
              */

          for (var i = 1; i <= res.context.rating; i++) {
            _html += '<i class="fas fa-star text-warning"></i>';
          }
          _html += "</div>";

          _html += "<p>" + res.context.review + "</p>";
          _html += "<h3>" + res.context.user + "</h3>";
          _html +=
            '<img src="https://th.bing.com/th?id=OIP.OesLvyzDO6AvU_hYUAT4IAHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2" alt=""/>';
          _html += "</div>";

          $(".swiper-wrapper").prepend(_html);
        }
      },
    });
  });
});
