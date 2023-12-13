const fs = require('fs');
const input = () => fs.readFileSync('/dev/stdin').toString().split('\n');

let [N, arr] = input()

N = Number(N)
arr = arr.split(' ').map(element => Number(element));

let minDistance = Infinity;

for(let i = 0; i < arr.length; i++){
    tempSum = 0;

    for(let j = 0; j < arr.length; j++){
        tempSum += Math.abs(i - j) * arr[j];
    }

    minDistance = Math.min(minDistance, tempSum);
}

console.log(minDistance)