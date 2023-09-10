/*
 * Load this script on the register page and profile page where new
 * passwords are being created to confirm that the password and confirm
 * password fields match and provide a custom html validation message
 * if they do not match.
 */

let password = document.getElementById("password");
let confirm_password = document.getElementById("confirm-password");

const confirmPassword = () => {
  if (password.value != confirm_password.value) {
    confirm_password.setCustomValidity("Passwords do not match");
  } else {
    confirm_password.setCustomValidity("");
  }
};

password.onchange = confirmPassword;
confirm_password.onkeyup = confirmPassword;
