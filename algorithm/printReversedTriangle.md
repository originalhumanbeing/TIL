# Level 1. 역삼각형 출력하기

### printReversedTriangle 메소드는 양의 정수 num을 매개변수로 입력받습니다. 다음을 참고해 *로 높이가 num인 삼각형을 문자열로 리턴하는 메소드를 완성하세요. num이 3일 때 다음과 같은 문자열을 리턴하면 됩니다.  
```javascript
***
**
*
```

[Hello World: 문제 링크](http://tryhelloworld.co.kr/challenge_codes/113) 

#### my Solution
```javascript
function printReversedTriangle(num) {
  var str = '*';
  var result = '';
  
  for(var i=num; i>=1; i--){
  	result += str.repeat(i) + '\n';	
  }
  return result;
}

console.log("결과 : " +'\n'+ printReversedTriangle(3));
```

#### Other Solutions
```javascript
// Seung*** Baek님의 풀이
function printReversedTriangle(num) {
  var result = ''
  while(num>0){result+=Array(num+1).join("*")+'\n';num--}

  return result
}

console.log("결과 : " +'\n'+ printReversedTriangle(3));
```

```javascript
// Goo*** Kim님의 풀이
function printReversedTriangle(num) {
  return '*'.repeat(num) + (num && '\n' + printReversedTriangle(num - 1) || '');
}

console.log("결과 : " +'\n'+ printReversedTriangle(3));
```

### 알아둘 것
- str.repeat();
count수만큼 str을 반복시킴, count가 음수이거나 무한일 때 RangeError를 throw함
```javascript
stringObj.repeat(count);
```
```javascript
"abc".repeat(3); // "abcabcabc"
```