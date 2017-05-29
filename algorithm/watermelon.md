# Level 1. 수박수박수박수박수박수?

### water_melon함수는 정수 n을 매개변수로 입력받습니다. 길이가 n이고, 수박수박수...와 같은 패턴을 유지하는 문자열을 리턴하도록 함수를 완성하세요. 예를 들어 n이 4이면 '수박수박'을 리턴하고 3이라면 '수박수'를 리턴하면 됩니다.

[Hello World: 문제 링크](http://tryhelloworld.co.kr/challenge_codes/107) 

#### my Solution1 
```javascript
function waterMelon(n){
    var result = "";
    for (var i = 0; i < n; i++){
        if(i%2 === 0) {
            result += '수';
        } else {
            result += '박';
        }
    }
    return result;
}

console.log("n이 3인 경우: "+ waterMelon(3));
```

#### my Solution2
```javascript
function waterMelon(n){
  var result = "";
  for (var i = 0; i < n; i++){
  	result += i%2===0? '수':'박';
  }
  return result;
}

console.log("n이 3인 경우: "+ waterMelon(3));
```

#### Other Solutions1
```javascript
// Jae N** jung님의 풀이
const waterMelon = n => {
    return '수박'.repeat(n/2) + (n%2 === 1 ? '수' : '');
}
```

#### Other Solutions2
```javascript
// 도*님의 풀이
function watermelon(n){
    var result = "수박";
    result = result.repeat(n-1).substring(0,n); 
    // n=3일 때, '수박수박' 반복된 것을 indexEnd 직전까지 부분집합으로 만드니까 '수박수'가 나옴
    
    return result;
}
```

####  알아둘 것
- String.prototype.repeat(count)
말 그대로 count 수만큼 str을 반복해 반환해준다.  
단, count는 다 정수로 환산되서 계산되고 음수나 분수는 넣을 수 없음.  
ECMAScript2015에 추가된 메소드이기 때문에 하위호환하려면 polyfill을 확인해보기!
```javascript
'abc'.repeat(-1); // rangeError
'abc'.repeat(0); // ''
'abc'.repeat(1); // 'abc'
'abc'.repeat(3.5); // 'abcabcabc' .5따위는 취급하지 않음
```

- String.prototype.substring()
```javascript
str.substring(indexStart[, indexEnd]);
```
indexStart ~ indexEnd 직전까지 전체 문자열의 부분 문자열을 반환함

```javascript
var a = 'mozilla';

// 1. indexStart가 indexEnd보다 큰 경우, 두 수를 바꿔서 substring 적용됨
a.substring(0,3); // 'moz'
a.substring(3,0); // 'moz

// 2. indexEnd 생략시 str.length가 indexEnd로 적용됨
a.substring(4,7); // 'lla'
a.substring(4); // 'lla'

// 3. indexEnd가 str.length보다 큰 경우에도 str.length가 indexEnd로 적용됨
a.substring(0,7); // 'mozilla'
a.substring(0,100); // 'mozilla'

// 4. index가 0보다 작거나 NaN인 경우, 0으로 취급됨
a.substring(0,'happy'); // ''
a.substring('happy',7); // 'mozilla'
a.substring(-5,7); 'mozilla'
```


