# Level 1. 삼각형 출력하기

### printTriangle 메소드는 양의 정수 num을 매개변수로 입력받습니다. 다음을 참고해 *로 높이가 num인 삼각형을 문자열로 리턴하는 printTriangle 메소드를 완성하세요. printTriangle이 return하는 String은 개행문자('\n')로 끝나야 합니다.
```
// num = 3
*
**
***
```

[Hello World: 문제 링크](http://tryhelloworld.co.kr/challenge_codes/101) 

#### my Solution
```javascript
function printTriangle(num) {
  var result = ''
	for (var i = 1; i <= num; i++){
  	result += '*'.repeat(i)+'\n';
  }
  return result;
}

console.log( printTriangle(3) );
```

### 알아둘 것: 문자열을 반복하고 싶다면 repeat()를 우선 생각해보자