//자바스크립트의 기본적인 재귀 피보나치

function fibo(n){
    if(n<=1){
        return n;
    }else{
        return fibo(n-2) + fibo(n-1)
    }
}

console.log(fibo(6))