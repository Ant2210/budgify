/*
 * This file contains the code to create the pie chart and bar chart
 * to show the percentage of income spent on each outgoing type and the
 * total of each outgoing type. It also contains the code to convert the
 * amounts in the budget table to currency format and the code to convert
 * the day of month to ordinal number.
 */

// Create variables to store the elements from the budget page
const allIncome = document.getElementsByClassName("income");
const totalIn = document.getElementById("total-in");
const allExpenses = document.getElementsByClassName("expense");
const totalOut = document.getElementById("total-out");
const disposableIncome = document.getElementById("disposable-income");
const currencies = document.getElementsByClassName("currency");
const dayOfMonths = document.getElementsByClassName("day-of-month");

const outgoingsPieChart = document.getElementById("pie-chart");
const outgoingsBarChart = document.getElementById("bar-chart");
const mortgages = document.getElementsByClassName("mortgage");
const utilities = document.getElementsByClassName("utility");
const transportCosts = document.getElementsByClassName("transport");
const unsecureds = document.getElementsByClassName("unsecured");
const comms = document.getElementsByClassName("comms");
const insurances = document.getElementsByClassName("insurance");
const childcareFees = document.getElementsByClassName("childcare");
const shoppings = document.getElementsByClassName("shopping");
const savings = document.getElementsByClassName("savings");
const others = document.getElementsByClassName("other");

/*
 * Get the total income and expenses from the budget table and set
 * the values of total in, total out and difference
 */

// Get the total income from budget table
let incomeTotal = 0;
for (let income of allIncome) {
  incomeTotal += parseFloat(income.innerHTML);
}
// Set the total income in the budget table
totalIn.innerText = incomeTotal;

// Get the total expenses from budget table
let expenseTotal = 0;
for (expense of allExpenses) {
  expenseTotal += parseFloat(expense.innerHTML);
}
// Set the total expenses in the budget table
totalOut.innerText = expenseTotal;

// Set the disposable income as the difference between income and expenses
// in the budget table, if the figure is positive the text will display
// in green, if negative it will display in red.
let totalDisposableIncome = incomeTotal - expenseTotal;
if (totalDisposableIncome < 0) {
  disposableIncome.classList.add("text-danger");
} else {
  disposableIncome.classList.add("text-success");
}
disposableIncome.innerText = incomeTotal - expenseTotal;

/*
 * Create a pie chart to show the percentage of income spent on each outgoing
 */

// Get the total of each outgoing
// Total of all expenses with the class name mortgage
let mortgageTotal = 0;
for (let mortgage of mortgages) {
  mortgageTotal += parseFloat(mortgage.innerText);
}

// Total of all expenses with the class name utility
let utilityTotal = 0;
for (let utility of utilities) {
  utilityTotal += parseFloat(utility.innerText);
}

// Total of all expenses with the class name transport
let transportTotal = 0;
for (let transport of transportCosts) {
  transportTotal += parseFloat(transport.innerText);
}

// Total of all expenses with the class name unsecured
let unsecuredTotal = 0;
for (let unsecured of unsecureds) {
  unsecuredTotal += parseFloat(unsecured.innerText);
}

// Total of all expenses with the class name comms
let commsTotal = 0;
for (let comm of comms) {
  commsTotal += parseFloat(comm.innerText);
}

// Total of all expenses with the class name insurance
let insuranceTotal = 0;
for (let insurance of insurances) {
  insuranceTotal += parseFloat(insurance.innerText);
}

// Total of all expenses with the class name childcare
let childcareTotal = 0;
for (let childcareFee of childcareFees) {
  childcareTotal += parseFloat(childcareFee.innerText);
}

// Total of all expenses with the class name shopping
let shoppingTotal = 0;
for (let shopping of shoppings) {
  shoppingTotal += parseFloat(shopping.innerText);
}

// Total of all expenses with the class name savings
let savingsTotal = 0;
for (let saving of savings) {
  savingsTotal += parseFloat(saving.innerText);
}

// Total of all expenses with the class name other
let otherTotal = 0;
for (let other of others) {
  otherTotal += parseFloat(other.innerText);
}

// Total disposable income for pie chart, if figure is negative set to 0
let totalDisposableIncomePie =
  totalDisposableIncome < 0 ? 0 : totalDisposableIncome;

// Calculate the percentage of income spent on each outgoing type, if
// no income return "No income provided"
const percentageOfIncome = (total) => {
  if (incomeTotal === 0) {
    return "- No income provided";
  } else {
    return ((total / incomeTotal) * 100).toFixed(2) + "%";
  }
};

// Create a pie chart and bar chart with insights if there is any income
// or expenses in the budget table
if (incomeTotal > 0 || expenseTotal > 0) {
  // Pie chart to show the percentage of income spent on each outgoing type
  new Chart(outgoingsPieChart, {
    type: "pie",
    data: {
      labels: [
        "Mortgage or Rent " + percentageOfIncome(mortgageTotal),
        "Utilities & Council Tax " + percentageOfIncome(utilityTotal),
        "Transport " + percentageOfIncome(transportTotal),
        "Unsecured Debt " + percentageOfIncome(unsecuredTotal),
        "Communications " + percentageOfIncome(commsTotal),
        "Insurances " + percentageOfIncome(insuranceTotal),
        "Childcare & School Fees " + percentageOfIncome(childcareTotal),
        "Shopping " + percentageOfIncome(shoppingTotal),
        "Savings & Investments " + percentageOfIncome(savingsTotal),
        "Other " + percentageOfIncome(otherTotal),
        "Disposable Income " + percentageOfIncome(totalDisposableIncomePie),
      ],
      datasets: [
        {
          label: "Outgoings",
          data: [
            mortgageTotal,
            utilityTotal,
            transportTotal,
            unsecuredTotal,
            commsTotal,
            insuranceTotal,
            childcareTotal,
            shoppingTotal,
            savingsTotal,
            otherTotal,
            totalDisposableIncomePie,
          ],
          backgroundColor: [
            "#54a1e9",
            "#e851e3",
            "#f5dd05",
            "#0000ff",
            "#187002",
            "#00ff00",
            "#acb52b",
            "#7308a5",
            "#ff0000",
            "#00aeae",
            "#fc7b3f",
          ],
          hoverOffset: 4,
        },
      ],
    },
    options: {
      plugins: {
        legend: {
          display: false, // Hide the legend
        },
      },
      responsive: true, // Make the chart responsive
      maintainAspectRatio: false, // Allow the aspect ratio to adjust
    },
  });

  // Bar chart to show the total of each outgoing
  new Chart(outgoingsBarChart, {
    type: "bar",
    data: {
      labels: [
        "Mortgage or Rent",
        "Utilities & Council Tax",
        "Transport",
        "Unsecured Debt",
        "Communications",
        "Insurances",
        "Childcare & School Fees",
        "Shopping",
        "Savings & Investments",
        "Other",
        "Disposable Income",
      ],
      datasets: [
        {
          label: "",
          data: [
            mortgageTotal,
            utilityTotal,
            transportTotal,
            unsecuredTotal,
            commsTotal,
            insuranceTotal,
            childcareTotal,
            shoppingTotal,
            savingsTotal,
            otherTotal,
            totalDisposableIncome,
          ],
          backgroundColor: [
            "#54a1e9",
            "#e851e3",
            "#f5dd05",
            "#0000ff",
            "#187002",
            "#00ff00",
            "#acb52b",
            "#7308a5",
            "#ff0000",
            "#00aeae",
            "#fc7b3f",
          ],
          hoverOffset: 4,
        },
      ],
    },
    options: {
      scales: {
        x: {
          display: false, // Hide x-axis labels
        },
        y: {
          display: true, // Hide y-axis labels
        },
      },
      plugins: {
        legend: {
          display: false, // Hide the top-level title
        },
      },
      responsive: true, // Make the chart responsive
      maintainAspectRatio: false, // Allow the aspect ratio to adjust
    },
  });
}

// Convert amounts in budget table to currency format
// Code found here https://shorturl.at/gjGW2
let gbp = new Intl.NumberFormat("en-GB", {
  style: "currency",
  currency: "GBP",
});

for (let currency of currencies) {
  currency.innerText = gbp.format(currency.innerText);
}

// Convert day of month to ordinal number
// Adapted code found here https://shorturl.at/knZ18
const numberToOrdinal = (n) => {
  if (n % 10 === 1 && n % 100 !== 11) {
    return `${n}st`;
  } else if (n % 10 === 2 && n % 100 !== 12) {
    return `${n}nd`;
  } else if (n % 10 === 3 && n % 100 !== 13) {
    return `${n}rd`;
  } else {
    return `${n}th`;
  }
};

for (let dayOfMonth of dayOfMonths) {
  dayOfMonth.innerText = numberToOrdinal(dayOfMonth.innerText);
}
