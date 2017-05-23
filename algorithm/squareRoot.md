# Level 1. 정수제곱근 판별하기

### nextSquare 함수는 정수 n을 매개변수로 입력받습니다. n이 임의의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 임의의 정수 x의 제곱이 아니라면 'no'를 리턴하는 함수를 완성하세요. 예를 들어 n이 121이라면 이는 정수 11의 제곱이므로 (11+1)의 제곱인 144를 리턴하고, 3이라면 'no'를 리턴하면 됩니다.  

[Hello World: 문제 링크](http://tryhelloworld.co.kr/challenge_codes/120) 

#### my Solution
```javascript
function nextSqaure(n){
  var result = 0;
  if (parseInt(Math.sqrt(n)) === Math.sqrt(n)) {
    result = Math.pow(Math.sqrt(n)+1, 2);
  } else {
  	result = "no";
  }
  return result;
}

console.log("결과 : " + nextSqaure(121));
```

#### Other Solutions
```javascript
// 윤*준님의 풀이
function nextSqaure(n){
  // 제곱근이 정수(integer)임을 이용한다.
  // Math.sqrt는 제곱근을 반환한다
  // Math.sqrt(9); // 3
  // Math.sqrt(2); // 1.414213562373095
  // parseInt(1.414213562373095); // 1
  var root = Math.sqrt(n);
  // if((parseInt(root) - root) === 0){
  //   return (root + 1 ) * (root + 1);
  // } else{
  //   return "no";
  // }
  var result = parseInt(root) - root === 0 ? (root + 1 ) * (root + 1) : "no";
  return result;
}

// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log("결과 : " + nextSqaure(121));
```

### 내장함수 정리
- Math.sqrt()
루트다 루트
```javascript
Math.sqrt(x)
// x가 음수인 경우에는 NaN을 리턴한다
```
```javascript
Math.sqrt(9); // 3
Math.sqrt(1); // 1
Math.sqrt(2); // 1.414blahblah
```

- Math.pow()
```javascript
Math.pow(base, exponent)
```
```javascript
Math.pow(2, 10); // 1024
```
