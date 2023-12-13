const fs = require('fs');
const inputAll = () => fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const print = (...args) => console.log(...args);

const calcDistance = (p1, p2) => {
    const [r1, c1] = p1;
    const [r2, c2] = p2;

    return Math.abs(r1 - r2) + Math.abs(c1 - c2);
}

let [N, ...arr] = inputAll()

N = Number(N)
arr = arr.map(line => line.split(' ').map(elm => Number(elm)))

let minDis = Infinity;

for(let skip = 1; skip < arr.length - 1; skip++){
    let tempDis = 0;
    let prevIdx = 0;

    for(let i = 1; i < arr.length; i++){
        if(i === skip) continue;

        tempDis += calcDistance(arr[prevIdx], arr[i]);
        prevIdx = i;
    }

    minDis = Math.min(minDis, tempDis);
}

print(minDis)