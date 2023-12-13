const fs = require('fs')
const inputAll = () => fs.readFileSync('/dev/stdin').toString().split('\n');
const print = (...arr) => console.log(...arr)

let [N, ...arr] = inputAll()

arr = arr.map(line => line.split(' ').map(elm => Number(elm)));

let maxCount = 0;

for(let i = 0; i < N; i++){
    for(let j = 0; j < N -2; j++){
        const tempCount = arr[i][j] + arr[i][j + 1] + arr[i][j + 2];
        maxCount = Math.max(tempCount, maxCount);
    }
}

print(maxCount);