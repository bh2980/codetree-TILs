const fs = require('fs');
const inputAll = () => fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const print = (...args) => console.log(...args);

let [N, ...arr] = inputAll();

N = Number(N);
arr = arr.map(elm => Number(elm));

let minSum = Infinity;

for(let start = 0; start < arr.length; start++){

    let tempSum = 0;

    for(let dis = 0; dis < arr.length; dis++){
        const currentIdx = (start + dis) % N;

        tempSum += arr[currentIdx] * dis;
    }

    minSum = Math.min(minSum, tempSum);
}

print(minSum);