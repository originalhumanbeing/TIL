# Level 1. 문자열 다루기 기본

### alpha_string46 함수는 문자열 s를 매개변수로 입력받습니다. s의 길이가 4 혹은 6이고, 숫자로만 구성되있는지 확인해주는 함수를 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

[Hello World: 문제 링크](http://tryhelloworld.co.kr/challenge_codes/99) 

#### my Solution
```javascript
function alpha_string46(s) {
  return (s.length == 4 || s.length == 6) && !!s.match(/^\d+$/);
}

console.log( alpha_string46("a234"));
console.log( alpha_string46("965"));
```

### 알아둘 것
- String.prototype.match()
```javascript
str.match(regexp)
// return값은 matching된 결과값들이 담긴 배열
// matching된 결과값이 없는 경우에는 null이 나옴
```