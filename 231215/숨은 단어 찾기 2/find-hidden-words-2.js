const fs = require('fs');
const inputAll = () => fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const print = (...args) => console.log(...args);

let [size, ...arr] = inputAll();

const [N, M] = size.split(' ').map(elm => Number(elm));
const CHAR_LIST = arr.map(line => Array.from(line));

function inRange(r, c){
    return 0 <= r && r < N && 0 <= c && c < M;
}

function zip(arr1, arr2){
    return Array.from({length: Math.min(arr1.length, arr2.length)}, (_, i) => [arr1[i], arr2[i]]);
}

function exploreLEE(CHAR_LIST, current, diff, length){
    const [cr, cc] = current;
    const [dr, dc] = diff;

    if(length === 3) return true;

    const [nr, nc] = [cr + dr, cc + dc];

    if(inRange(nr, nc) && CHAR_LIST[nr][nc] === 'E') return exploreLEE(CHAR_LIST, [nr, nc], diff, length + 1);

    return false;
}

function solution(CHAR_LIST){
    let count = 0;

    const drs = [0, -1, 0, 1, -1, -1, 1, 1];
    const dcs = [-1, 0, 1, 0, -1, 1, -1, 1];

    for(let i = 0; i < N; i++){
        for(let j = 0; j < M; j++){
            if(CHAR_LIST[i][j] === 'L'){
                for(const diff of zip(drs, dcs)){
                    if(exploreLEE(CHAR_LIST, [i, j], diff, 1)){
                        count++;
                    }
                }
            }
        }
    }

    return count;
}

print(solution(CHAR_LIST));