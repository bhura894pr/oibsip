let display = document.getElementById('inputBox');
let buttons = document.querySelectorAll('button');

let buttonsArray = Array.from(buttons);
let string = '';
let ans = '';

buttonsArray.forEach(btn => {
    btn.addEventListener('click', (e) => {
        let value = e.target.innerHTML;

        if (value == 'DEL') {
            string = string.substring(0, string.length - 1);
            display.value = string;
        } else if (value == 'AC') {
            string = '';
            display.value = string;
        } else if (value == 'ENTER') {
            try {
                // Replace '%' with '/100' to handle percentage calculations
                string = string.replace(/%/g, '/100');
                string = eval(string);
                display.value = string;
                ans = string;
            } catch (error) {
                display.value = 'Error';
            }
        } else if (value == 'ANS') {
            string += ans;
            display.value = string;
        } else if (value == '√') {
            try {
                string = Math.sqrt(eval(string)).toString();
                display.value = string;
                ans = string;
            } catch (error) {
                display.value = 'Error';
            }
        } else if (value == '±') {
            if (string.charAt(0) === '-') {
                string = string.substring(1);
            } else {
                string = '-' + string;
            }
            display.value = string;
        } else {
            string += value;
            display.value = string;
        }
    });
});
