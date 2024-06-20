document.addEventListener('DOMContentLoaded', function() {
    const inputTemp = document.getElementById('inputTemp');
    const inputUnit = document.getElementById('inputUnit');
    const outputTemp = document.getElementById('outputTemp');
    const outputUnit = document.getElementById('outputUnit');

    function convertTemperature() {
        let temp = parseFloat(inputTemp.value);
        let fromUnit = inputUnit.value;
        let toUnit = outputUnit.value;

        switch (fromUnit) {
            case 'F':
                temp = (temp - 32) * (5 / 9);
                break;
            case 'K':
                temp -= 273.15;
                break;
            case 'R':
                temp = (temp - 491.67) * (5 / 9);
                break;
            default:
                break;
        }

        switch (toUnit) {
            case 'F':
                temp = (temp * 9 / 5) + 32;
                break;
            case 'K':
                temp += 273.15;
                break;
            case 'R':
                temp = (temp + 273.15) * (9 / 5);
                break;
            default:
                break;
        }

        outputTemp.value = temp.toFixed(2);
    }

    inputTemp.addEventListener('input', convertTemperature);
    inputUnit.addEventListener('change', convertTemperature);
    outputUnit.addEventListener('change', convertTemperature);

    convertTemperature();
});
