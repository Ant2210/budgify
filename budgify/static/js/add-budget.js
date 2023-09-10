  /* 
  *Set the focus to the input field when the modal is shown
  */
  // Get a reference to the modal element
  const addBudgetModal = document.getElementById('add-budget-modal');

  // Listen for the modal's shown.bs.modal event using an arrow function
  addBudgetModal.addEventListener('shown.bs.modal', () => {
    // Get a reference to the input field
    const inputField = document.getElementById('budget_name');

    // Set the focus on the input field
    inputField.focus();
  });