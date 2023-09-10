// Countdown time that redirects to home page after 5 seconds
const countdownTimer404 = document.getElementById("countdown-timer-404");

document.addEventListener("DOMContentLoaded", function () {
  let timeLeft = 5;
  const interval = setInterval(() => {
    timeLeft--;
    countdownTimer404.innerHTML = timeLeft;
    if (timeLeft <= 0) {
      clearInterval(interval);
      window.location.href = "/";
    }
  }, 1000);
});
