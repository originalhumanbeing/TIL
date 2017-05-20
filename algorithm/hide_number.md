# Level 1. 핸드폰 번호 가리기

### 별이는 헬로월드텔레콤에서 고지서를 보내는 일을 하고 있습니다. 개인정보 보호를 위해 고객들의 전화번호는 맨 뒷자리 4자리를 제외한 나머지를 "*"으로 바꿔야 합니다. 전화번호를 문자열 s로 입력받는 hide_numbers 함수를 완성해 별이를 도와주세요. 예를 들어 s가 "01033334444"면 "*******4444"를 리턴하고 "027778888"인 경우는 "*****8888"을 리턴하면 됩니다.  
[Hello World: 문제 링크](http://tryhelloworld.co.kr/challenge_codes/132) 

#### my Solution 1
처음으로 푸는 알고리즘 문제다보니 푸는데 급급했다.  
s는 문자열이라고 했는데 숫자라고 생각하고 굳이 형변환하고  
for문을 두 번이나 쓰고... 그야말로 난장판
```javascript
function hide_numbers(s){
  var result = ""
  result = String(s).split('');
  for(var i=0; i < result.length - 4; i++){
		result[i] = "*";
	}
  for(var j=0; j < result.length - 1; j++){
		result = result.toString().replace(",", "");
	}
  return result;
}

console.log("결과 : " + hide_numbers('01033334444'));
```

#### my Solution 2  
```javascript
function hide_numbers(s){
  var result = ""
  return result = s.split('').map((k,i,a)=>{
		if(i < a.length - 4)
			return "*";
		else 
      return k;
	}).join('');
}

console.log("결과 : " + hide_numbers('01033334444'));
```

#### 활용한 생성자 및 메소드 정리
- String()  
문자열 생성자로 이를 통해서 생성된 문자열은 primitive strings임. (type이 string 나옴)
- Array.prototype.toString()  
배열의 각 요소를 ','로 합쳐서(join) 문자열로 반환함
```javascript
var months = ['Jan', 'Feb', 'Mar'];
var monthString = months.toString(); // 'Jan,Feb,Mar'
```
** String()과 toString()은 거의 항상 같은 결과를 가짐. 다만, toString()은 null, undefined값에 쓰려고 하면 typeError나고 String()은 그 자체를 문자열로 만들어 버림.  

- String.prototype.split()
String을 substrings로 나누고, 그 substrings를 각각 요소로 삼아 배열을 만드는 메소드.  
```javascript
str.split([separator[, limit]]) 
// separator를 생략하면 전체 문장이 하나의 배열 요소가 됌 (길이가 1인 배열)
```

- String.prototype.replace()
어떤 패턴에 일치되는 일부 또는 전 부분이 교체된 새로운 문자열을 반환함.  
정규식, 함수도 매개변수로 사용할 수 있음.  
```javascript
var re = /apples/gi;
var str = 'Apples are round, and apples are juicy'
var newstr = str.replace(re, 'oranges');
console.log(newstr); // oranges are round, and oranges are juicy
```

- Array.prototype.map()
배열 내의 모든 요소를 돌아가며 콜백함수로 처리하여 새로운 배열을 반환함.  
callback함수는 배열값이 들어있는 인덱스에 대해서만 호출됨. 즉, 삭제된 값이나 할당되지 않은 값에는 호출되지 않음.  
map이 호출된 이후에 배열에 추가된 요소들도 callback에 호출되지 않음.  
```javascript
arr.map(callback[, thisArg])
// callback: currentValue/ index/ array(원래 배열)
// thisArg: callback을 실행할 때 this로 사용되는 값. 기본값은 window 객체
``` 
```javascript
var numbers = [1, 4, 9];
var roots = numbers.map(Math.sqrt);
// roots = [1, 2, 3]

var kvArray = [{key:1, value:10}, {key:2, value:20}, {key:3, value:30}];
var reformattedArray = kvArray.map(function(obj){
    var rObj = {};
    rObj[obj.key] = obj.value;
    return rObj;
});
// reformattedArray = [{1:10}, {2:20}, {3:30}];

var numbers = [1,4,9];
var doubles = numbers.map(function(num){
    return num * 2;
});
// double = [2,8,18];
// numbers = [1,4,9];

var map = Array.prototype.map;
var a = map.call('Hello World', function(x){return x.charCodeAt(0); });
// a = [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100];

var elems = document.querySelectorAll('select option:checked');
var values = [].map.call(elems, function(obj){
    return obj.value;
})
// 스크린에 선택된 옵션들을 return

var str = '12345';
[].map.call(str, function(x){
    return x;
}).reverse().join(''); // '54321'
// reverse도 array 메소
```

- Array.prototype.join()
배열의 모든 요소를 하나로 연결해서 문자열을 만드는 메소드.  
```javascript
str = arr.join([separator = ','])
// separator는 배열의 각 요소를 구분할 문자열을 지정함.
// 생략하면 쉼표로 구분되고 빈 문자열이면 띄어쓰기 없이 이어진 문장 생성.
```
```javascript
var a = ['summer', 'autumn', 'winter'];
var val1 = a.join(); // summer,autumn,winter;
var val2 = a.join(''); // summerautumnwinter;
var val3 = a.join(', '); // summer, autumn, winter;
```

#### reference
[JavaScript MDN 사이트](https://developer.mozilla.org/ko/docs/Web/JavaScript)
