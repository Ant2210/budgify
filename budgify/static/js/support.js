const loader = document.getElementById("loader");
const supportEmailForm = document.getElementById("support-form");
const successMessage = document.getElementById("success-message");
const errorMessage = document.getElementById("error-message");
const countdownTimer = document.getElementById("countdown-timer");
const closeModalBtn = document.getElementById("close-modal");

const sendMail = (supportForm) => {
  // Show loader
  loader.classList.remove("d-none");
  // Send email via emailjs
  emailjs
    .send("gmail", "Budgify", {
      from_name: supportForm.name.value,
      from_email: supportForm.email.value,
      message: supportForm.message.value,
    })
    .then(
      (response) => {
        // Hide loader
        loader.classList.add("d-none");
        // reset form after submission
        supportEmailForm.reset();
        // Show success message
        successMessage.classList.remove("d-none");
        // Start countdown and close Modal after 5 seconds
        let timeLeft = 5;
        const interval = setInterval(() => {
          timeLeft--;
          countdownTimer.innerHTML = timeLeft;
          if (timeLeft <= 0) {
            clearInterval(interval); // Stop the interval
            closeModalBtn.click(); // Close Modal
            successMessage.classList.add("d-none");
            countdownTimer.innerHTML = "5"; // Clear the countdown timer
          }
        }, 1000);
      },
      (error) => {
        // Hide loader
        loader.classList.add("d-none");
        // Show error message for 5 seconds
        errorMessage.classList.remove("d-none");
        setTimeout(() => {
          errorMessage.classList.add("d-none");
        }, 5000);
      }
    );

  return false;
};
