$('.navTrigger').click(function () {
    $(this).toggleClass('active');
    console.log("Clicked menu");
    $("#mainListDiv").toggleClass("show_list");
    $("#mainListDiv").fadeIn();

});

$(".img-fluid").addClass("wow fadeIn z-depth-1-half");

new WOW().init();

$(function() {
  
    //modal
  const modal = $(".modal");
  const modalToggle = $(".modal-toggle");
  const modalWrapper = $(".modal-wrapper");
  const modalHeight = modalWrapper.height();

  //countdown
  function coundDown() {
    console.log("countdown");
    var countdownNumberEl = document.getElementById("countdown-number");
    var countdown = 5;
    countdownNumberEl.textContent = countdown;
    var downloadTimer = setInterval(function() {
      countdown--; // 5 to 0
      countdownNumberEl.textContent = countdown;

      if (countdown > 0) {
        modalToggle.unbind("click", showMConfirmModal);
      } else {
        modalToggle.bind("click", showMConfirmModal);
        clearInterval(downloadTimer);
        modal.removeClass("is-visible");
      }
    }, 1000);
  }


  //show modal
  function showMConfirmModal(e) {
    console.log('icon click');
    const modalPosY = $(document).outerHeight() / 2 - modalHeight/2;
    modalWrapper.css("margin-top", modalPosY)
    //fire countedown modal
    if ($("#count-loading").length) {
      e.preventDefault();
      modal.addClass('is-visible');
      coundDown();
    }else{
      //fire confirm modal
      e.preventDefault();
      modal.toggleClass('is-visible');
    }
  }

  modalToggle.click(showMConfirmModal);
  
  $(".btn-cancel").click(function(e) {
    modal.removeClass("is-visible");
  });
});
