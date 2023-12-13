const fs = require('fs')
const inputAll = () => fs.readFileSync('/dev/stdin').toString().split('\n')

let [N, arr] = inputAll();

N = Number(N);
arr = arr.split(' ').map(elm => Number(elm));
const LENGTH = arr.length;

let count = 0;

for(let i = 0; i < LENGTH; i++){
    for(let j = i + 1; j < LENGTH; j++){
        for(let k = j + 1; k < LENGTH; k++){
            if(arr[i] <= arr[j] && arr[j] < arr[k]){
                count++;
            }
        }
    }
}

console.log(count);