const fs = require('fs');
// const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
// let input = fs.readFileSync(filePath).toString().trim().split("\n");
let input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");

const [N, M] = input[0].split(' ').map(Number);
const arr = []

for (let i = 1; i < N+1; i++) {
    const arr_tmp = input[i].split(' ').map(Number);
    arr.push(arr_tmp);   
}
const K = Number(input[N+1])

for (let idx = N+2; idx < K+N+2; idx++) {
    const [a, b, x, y] = input[idx].split(' ').map(Number);
    let sum = 0
    // console.log(info)
    for (let i = a-1; i < x; i++) {
        for (let j = b-1; j < y; j++) {
            sum += arr[i][j];
        }
    }
    console.log(sum)
}

