# Level 1. 짝수와 홀수

### evenOrodd 메소드는 int형 num을 매개변수로 받습니다. num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하도록 evenOrOdd에 코드를 작성해 보세요. num은 0 이상의 정수이며, num이 음수인 경우는 없습니다.  

[Hello World: 문제 링크](http://tryhelloworld.co.kr/challenge_codes/122) 

#### my Solution
```javascript
function evenOrOdd(num) {
  if (num % 2 === 0){
  	return "Even"
  } else {
  	return "Odd"
  }
}

console.log("결과 : " + evenOrOdd(2));
console.log("결과 : " + evenOrOdd(3));
```

#### Other Solutions
```javascript
// atom의 풀이
function evenOrOdd(num) {
  return (num % 2)? "Odd":"Even";
}

console.log("결과 : " + evenOrOdd(2));
console.log("결과 : " + evenOrOdd(3));
```
num % 2 === 0일 때, 0이 거짓이라는 것을 활용해서  
0 -> 거짓 -> 우항의 값 -> 'even'을 리턴하게 만들었다

#### JavaScript의 'false'값
- 값이 없거나 0, -0, null, false, NaN, undefined, 빈 문자열('')은 모두 false  
- false 값을 가진 Boolean 객체 + undefined, null 값 이외의 모든 값을 가진 가진 객체들은 조건문에서 true  
```javascript
x = new Boolean(false);
if (x) {
    // .... 조건 x는 참으로 인정되어 코드가 실행됨
}  
```
```javascript
y = false;
if (y) {
    // .... 조건 y가 false여서 코드가 실행되지 않
}
```

#### reference
[JavaScript MDN: Boolean](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
