# Level 1. 평균 구하기

### def average(list): 함수를 완성해서 매개변수 list의 평균값을 return하도록 만들어 보세요. 어떠한 크기의 list가 와도 평균값을 구할 수 있어야 합니다.  

[Hello World: 문제 링크](http://tryhelloworld.co.kr/challenge_codes/126) 

#### my Solution
```javascript
function average(array){
  var sum = 0;
  var leng = array.length;
  
  for(var i=0; i<leng; i++){
  	sum += array[i];
  }
  
  var ave = sum/leng;
  
  return ave;
}

var testArray = [5,3,4,2,1] 
console.log("평균값 : " + average(testArray));
```

#### Other Solutions
you can write much simpler code using reduce method!
```javascript
// Haydn Hyundong Kim의 풀이

function average(array){
    return array.reduce((a,b) => a+b)/array.length;
}
```

#### 메소드 정리
- Array.prototype.reduce()
배열의 각 값을 왼쪽에서 오른쪽 방향으로 누산할 수 있는 메소드.  
```javascript
arr.reduce(callback[, initialValue])
// callback은 previousValue, currentValue, 
// currentIndex, array를 인수로 포함될 수 있음
// initialValue는 callback의 초기값으로
// 계산 전부터 초기값이 +,-... 등 될 수 있게 설정 가능
```
```javascript
var total = [0, 1, 2, 3].reduce(function(a,b){
    return a+b;
});
// total = 6;

var total2 = [0, 1, 2, 3, 4].reduce(function(prev, curr, currIndex, arr){
    return prev+curr;
}, 10); // init값 10;
// total2 = 20;
```

#### reference
[JavaScript MDN: reduce](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce)

