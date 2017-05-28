# Level 1. 스트링을 숫자로 바꾸기

### strToInt 메소드는 String형 str을 매개변수로 받습니다. str을 숫자로 변환한 결과를 반환하도록 strToInt를 완성하세요. 예를 들어 str이 "1234"이면 1234를 반환하고, "-1234"이면 -1234를 반환하면 됩니다. str은 부호(-,+)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다. 

[Hello World: 문제 링크](http://tryhelloworld.co.kr/challenge_codes/110) 

#### my Solution
```javascript
function strToInt(str){
  return Number(str);
}

console.log(strToInt("-1234"));
```

### 알아둘 것
- 문자열을 숫자로 형 변환하는 법: Number(), parseInt()를 활용하자  
typeof()를 했을 때 Number(), parseInt()는 둘 다 number로 나옴,  
그러나 ** 형을 조금 더 명시적으로 표현하고 싶다면 parseInt(str, 진수)나 parseFloat()를 사용하자 **

- 절대값으로 바꾸고 싶다면: Math.abs()를 쓰면 된다
```javascript
Math.abs('-1'); // 1
Math.abs(-2); // 2
Math.abs(); // NaN
Math.abs(null); // 0
```
