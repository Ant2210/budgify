const allIncome = document.getElementsByClassName('income');
const totalIn = document.getElementById('total-in');
const allExpenses = document.getElementsByClassName('expense');
const totalOut = document.getElementById('total-out');
const difference = document.getElementById('difference');

// Get the total income from budget table
let incomeTotal = 0;
for (let i = 0; i < allIncome.length; i++) {
  incomeTotal += parseFloat(allIncome[i].innerHTML);
}

// Set the total income in the budget table
totalIn.innerText = incomeTotal;

// Get the total expenses from budget table
let expenseTotal = 0;
for (let i = 0; i < allExpenses.length; i++) {
  expenseTotal += parseFloat(allExpenses[i].innerHTML);
}

// Set the total expenses in the budget table
totalOut.innerText = expenseTotal;

// Set the difference between income and expenses in the budget table
difference.innerText = incomeTotal - expenseTotal;
