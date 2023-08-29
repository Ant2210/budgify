let password = document.getElementById("password")
let confirm_password = document.getElementById("confirm-password");

const confirmPassword = () => {
  if(password.value != confirm_password.value) {
    confirm_password.setCustomValidity("Passwords do not match");
  } else {
    confirm_password.setCustomValidity('');
  }
}

password.onchange = confirmPassword;
confirm_password.onkeyup = confirmPassword;