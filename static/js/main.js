$(document).ready(function () {
  // Init Sidenav
  $('.button-collapse').sideNav();

  // Scrollspy
  $('.scrollspy').scrollSpy();

  // Modal Trigger
  $('.modal').modal({
    dismissible: true,
    inDuration: 300,
    outDuration: 200,
  });

  // Swipeable Tabs
  $('#tabs-swipe').tabs({
    swipeable: true,
    height: 100,
  });

  // Collapsible Sida Nav
  $('.collapsible').collapsible();

  // DropDown
  $('.dropdown-trigger').dropdown({
    inDuration: 300,
    outDuration: 225,
    hover: true,
    belowOrigin: true,
    alignment: 'right',
  });

  // Swipeable Tabs Height

  // Select Option In Apply Now Form
  // INIT SELECT LIST
  $('select').material_select();

  // Navbar Transparency
  $(window).scroll(function () {
    if ($(window).scrollTop() > 105) {
      $('.navScroll').addClass('grey lighten-5');
      $('.text-black').addClass('black-text');
    } else {
      $('.navScroll').removeClass('grey lighten-5');
      $('.text-black').removeClass('black-text');
    }
  });
  // Go To Top Floating Button(Disable At Top)
  $(window).scroll(function () {
    if ($(window).scrollTop() > 220) {
      $('.fixed-action-btn').fadeIn('500');
    } else {
      $('.fixed-action-btn').fadeOut('500');
    }
  });

  // ScrollFire
  const options = [
    {
      selector: '.main-text',
      offset: 0,
      callback: function (el) {
        Materialize.fadeInImage($(el));
      },
    },
  ];
});
