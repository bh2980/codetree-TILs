const fs = require('fs');
const inputAll = () => fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const print = (...args) => console.log(...args);

let [N, arr] = inputAll();
N = Number(N);
arr = arr.split(' ').map(elm => Number(elm));

let count = 0;

for(let s = 0; s < N; s++){
    for(let e = s + 1; e <= N; e++){
        let tempSum = 0;

        for(let idx = s; idx < e; idx++){
            tempSum += arr[idx];
        }

        const avg = tempSum / (e - s);

        let includeFlag = false;

        for(let idx = s; idx < e; idx++){
            if(arr[idx] === avg){
                includeFlag = true;
                break;
            }
        }

        if(includeFlag) count++;
    }
}

print(count);