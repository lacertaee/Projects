let buttons = Array.from(document.querySelectorAll("button"));
const operators = buttons.filter((x) => x.classList.contains("operator"));
buttons = buttons.filter((x) => !x.classList.contains("operator"));
const sheet = document.querySelector(".operations");
let pressed = false;
let first = 0;
let second = 0;
let operation = "";

document.addEventListener("DOMContentLoaded", () => {
  operators[4].addEventListener("click", () => {
    calculate();
  });
  for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", () => {
      check(buttons[i]);
    });
  }
  for (let i = 0; i < operators.length - 1; i++) {
    operators[i].addEventListener("click", () => {
      if (sheet.innerHTML !== "0") {
        operate(operators[i]);
      }
    });
  }
});

function check(button) {
  let number = Number(sheet.innerHTML);
  switch (button.innerHTML) {
    case "AC":
      if (sheet.innerHTML !== "0") {
        sheet.innerHTML = "0";
      }
      break;
    case "+/-":
      number = number * -1;
      sheet.innerHTML = String(number);
      break;
    case "%":
      number = number / 100;
      sheet.innerHTML = String(number);
      break;
    default:
      let num = "";
      if (!isNaN(Number(button.innerHTML))) {
        num = button.innerHTML;
      }
      if (button.innerHTML === ".") {
        num = ".";
      }
      if (number === 0 || num === "") {
        sheet.innerHTML = num;
      } else {
        sheet.innerHTML += num;
      }
  }
}

function operate(button) {
  let number = Number(sheet.innerHTML);
  first = number;
  switch (button.innerHTML) {
    case "/":
      check(button);
      operation = "/";
      break;
    case "x":
      check(button);
      operation = "x";
      break;
    case "-":
      check(button);
      operation = "-";
      break;
    case "+":
      check(button);
      operation = "+";
      break;
  }
}

function calculate() {
  second = Number(sheet.innerHTML);
  let result = 0;
  switch (operation) {
    case "/":
      result = first / second;
      break;
    case "x":
      result = first * second;
      break;
    case "-":
      result = first - second;
      break;
    case "+":
      result = first + second;
      break;
  }
  sheet.innerHTML = result;
}
