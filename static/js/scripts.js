function autoType(elementClass, typingSpeed) {
  var thhis = $(elementClass);
  thhis.css({
    "position": "relative",
    "display": "inline-block"
  });
  thhis.prepend('<div class="cursor" style="right: initial; left:0;"></div>');
  thhis = thhis.find(".welcome-text");
  var text = thhis.text().trim().split('');
  var amntOfChars = text.length;
  var newString = "";
  thhis.text("|");
  setTimeout(function () {
    thhis.css("opacity", 1);
    thhis.prev().removeAttr("style");
    thhis.text("");
    for (var i = 0; i < amntOfChars; i++) {
      (function (i, char) {
        setTimeout(function () {
          newString += char;
          thhis.text(newString);
        }, i * typingSpeed);
      })(i + 1, text[i]);
    }
  }, 1500);
}

$(document).ready(function () {
  // Now to start autoTyping just call the autoType function with the 
  // class of outer div
  // The second paramter is the speed between each letter is typed.   
  autoType(".welcome-type", 200);

  $('.more-click').click(function () {
    $('.more').toggle();
  });
});

document.addEventListener('DOMContentLoaded', function () {
  let stars = document.querySelectorAll('.star');
  stars.forEach(function (star) {
    star.addEventListener('click', setRating);
  });

  let rating = parseInt(document.querySelector('.stars').getAttribute('data-rating'));
  let target = stars[rating - 1];
  target.dispatchEvent(new MouseEvent('click'));
});

function setRating(ev) {
  let span = ev.currentTarget;
  let stars = document.querySelectorAll('.star');
  let match = false;
  let num = 0;
  stars.forEach(function (star, index) {
    if (match) {
      star.classList.remove('rated');
    } else {
      star.classList.add('rated');
    }
    //are we currently looking at the span that was clicked
    if (star === span) {
      match = true;
      num = index + 1;
    }
  });
  document.querySelector('.stars').setAttribute('data-rating', num);
}