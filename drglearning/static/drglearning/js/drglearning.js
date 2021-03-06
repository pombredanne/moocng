(function ($) {
  init = function () {
    var drglearningHost = $("#drglearning-host").val();
        urlToEmbed = $("#career-url").val(),
        iframe = $("#career-iframe"),
        title = $("#career-title");
        playerCode = $("#player-code").val();

    $("a.career-id").each(function (e) {
      var $this = $(this);
      $this.on("click", function (elto) {
        var careerId = $this.data("career-id"),
            careerCode = $this.data("career-code"),
            origin = window.location.protocol + "//" + window.location.host,
            src = urlToEmbed + careerId +"&import="+ origin +"#"+ encodeURIComponent(document.location.href);
        title.text($this.text());
        iframe.attr("src", src);

        XD.receiveMessage(function (message) {
          if (message.origin !== drglearningHost) {
            return;
          }
          if (message.data.action == "getPlayerCode") {
            args = {"action": "postPlayerCode", "params": {"playerCode": playerCode}};
            XD.postMessage(args, src, frames[0]);
          }
          if (message.data.action == "getCourseCode") {
            args = {"action": "postCourseCode", "params": {"id": careerId, "courseCode": careerCode}};
            XD.postMessage(args, src, frames[0]);
          }
        }, drglearningHost);

        return false;
      });
    });

    $("a.career-id:first").click();
  };
  $(document).ready(init);
})(jQuery);
