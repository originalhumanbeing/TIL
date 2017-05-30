# Level 1. 서울에서 김서방 찾기

### findKim 함수(메소드)는 String형 배열 seoul을 매개변수로 받습니다. seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하세요. seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

[Hello World: 문제 링크](http://tryhelloworld.co.kr/challenge_codes/104) 

#### my Solution
```javascript
function findKim(seoul){
  var idx = 0;
    for(var i = 0; i < seoul.length; i++) {
    if (seoul[i] === "Kim") {
        idx = i;
    }
  }
  return "김서방은 " + idx + "에 있다";
}

console.log( findKim(["Queen", "Tod", "Kim"]));
```

#### Other Solutions
```javascript
// 장*혁님의 풀이
function findKim(seoul){
  var idx = seoul.indexOf('Kim');

  return "김서방은 " + idx + "에 있다";
}

console.log( findKim(["Queen", "Tod", "Kim"]));
```

### 알아둘 것: indexOf는 str에만 있는 것이 아니었다!
- Array.prototype.indexOf()
- String.prototype.indexOf()