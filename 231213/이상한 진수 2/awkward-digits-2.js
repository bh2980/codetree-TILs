const fs = require('fs')
const inputAll = () => fs.readFileSync('/dev/stdin').toString().split('\n');
const print = (...args) => console.log(...args);

const [binStr] = inputAll();
const binArr = Array.from(binStr);

for(let i = 0; i < binArr.length; i++){
    const binChar = binArr[i];

    if(binChar === '0'){
        binArr[i] = '1';

        print(parseInt(binArr.join(''), 2));
        return;
    }
}

binArr[binArr.length - 1] = '0'
print(parseInt(binArr.join(''), 2));