# 제어문 (Control-Flow)
- 코드의 흐름(flow)을 제어(control)하는 문(Statement)
- 기본적으로 좌->우, 상->하로 실행되는 흐름을 분기문, 반복문 등을 활용하여 제어한다  
 
## 1. 분기문 (=조건문)
- 분기의 사전적 의미: 갈래가 나누어 지다
- 위 사전적 의미에서도 알 수 있듯이 분기문을 만나면 조건, 경우에 따라 다른 코드가 실행된다  
1) if
2) switch
 
## 2. 반복문
- 반복문을 만나면 해당하는 부분이 조건이 만족될 때까지 반복적으로 수행된다  
1) for: 특정 조건이 거짓이 될 때까지 반복
```javascript
for([초기문]; [조건문]; [증감문]) {
    // 반복 수행하고자 하는 코드
}
// 실행 순서
// 1. 초기문 실행
// 2. 조건문 검사
// 3. 조건문이 참일 경우 내부 코드 수행
// 4. 증감문 실행
// 5. 조건문 검사 후 참일 경우 내부 코드 수행
// 위 과정 반복
```
```html
<form name="selectForm">
  <p>
    <label for="musicTypes">Choose some music types, then click the button below:</label>
    <select id="musicTypes" name="musicTypes" multiple="multiple">
      <option selected="selected">R&B</option>
      <option>Jazz</option>
      <option>Blues</option>
      <option>New Age</option>
      <option>Classical</option>
      <option>Opera</option>
    </select>
  </p>
  <p><input id="btn" type="button" value="How many are selected?" /></p>
</form>

<script>
function howMany(selectObject) {
  var numberSelected = 0;
  for (var i = 0; i < selectObject.options.length; i++) {
    if (selectObject.options[i].selected) {
      numberSelected++;
    }
  }
  return numberSelected;
}

var btn = document.getElementById("btn");
btn.addEventListener("click", function(){
  alert('Number of options selected: ' + howMany(document.selectForm.musicTypes))
});
</script>
```

2) do...while: 특정 조건이 거짓이 될 때까지 반복, 단, 무조건 1회는 실행됨  
```javascript
do {
    // 반복 수행하고자 하는 코드
}
while (조건문);
```
```javascript
do {
  i += 1;
  console.log(i);
} while (i < 5);
```

3) while: 조건이 참이기만 하면 계속 반복
```javascript
while(조건문) {
    // 반복 수행하고자 하는 코드
}
```
```javascript
n = 0;
x = 0;
while (n < 3) {
  n++;
  x += n;
}
```

4) 레이블: 프로그램 내의 다른 곳을 참조할 수 있도록 식별자로 문을 제공함  
```javascript
label:
    statement
```
```javascript
markLoop:
while (theMark == true) {
    doSomething();
}
```

5) break: 반복문, switch문, 레이블 문과 결합한 문 탈출 시 사용
```
break; // 레이블 없이 break문만 쓸 경우
break 레이블; // 레이블 문을 쓸 때, 특정 레이블 문에서 종료
```
```javascript
var x = 0;
var z = 0
labelCancelLoops: while (true) {
  console.log("Outer loops: " + x);
  x += 1;
  z = 1;
  while (true) {
    console.log("Inner loops: " + z);
    z += 1;
    if (z === 10 && x === 10) {
      break labelCancelLoops;
    } else if (z === 10) {
      break;
    }
  }
}
```
6) continue: while, do-while, for, 레이블 문을 재시작하기 위해 사용  
```
continue; // 레이블 없이 사용시, 현재 반복 종료하고 다음 코드를 실행함
continue label; // 해당 레이블로 식별되는 루프 문에만 적용됨
```
```javascript
i = 0;
n = 0;
while (i < 5) {
  i++;
  if (i == 3) {
    continue;
  }
  n += i;
}
// n = 1, 3, 7, 12
```
```javascript
checkiandj:
  while (i < 4) {
    console.log(i);
    i += 1;
    checkj:
      while (j > 4) {
        console.log(j);
        j -= 1;
        if ((j % 2) == 0) {
          continue checkj;
        }
        console.log(j + " is odd.");
      }
      console.log("i = " + i);
      console.log("j = " + j);
  }
```

7) for...in: 객체 내의 속성들을 순서대로 돌려가며 특정 코드를 적용시킴
```javascript
for (variable in object){
    // statements
}
```
```javascript
function dump_props(obj, obj_name) {
  var result = "";
  for (var i in obj) {
    result += obj_name + "." + i + " = " + obj[i] + "<br>";
  }
  result += "<hr>";
  return result;
}
```
8) for...of: for...in과 동일하게 반복하며 특정 코드를 수행, 단 반환되는 결과값이 다름  

```
for (variable of object) {
  //statement
}
```

* for...in/ for...of 차이점 예시
```
let arr = [3, 5, 7];
arr.foo = "hello";

for (let i in arr) {
   console.log(i); // logs "0", "1", "2", "foo"
}

for (let i of arr) {
   console.log(i); // logs "3", "5", "7"
}
```

# 함수 (Function)
- 작업을 수행하거나 값을 계산하는 문장의 집합

## 1. 내장함수
- JavaScript 내의 미리 정의된 함수들
1. eval()
2. isFinite()
3. isNan()
4. parseInt()

- 중첩된 함수 중 내부에 존재하는 함수를 내장함수라고 부르기도 함  
```javascript
function outer(num1){
    var num2 = 5;
    function inner(){
        return num1 * num2;
    }
    return inner();
}
```

## 2. 외장함수
- 중첩된 함수 중 바깥에 존재하는 함수  
```javascript
var pet = function(name) {   // 외부 함수는 'name'이라 불리는 변수를 저장합니다.
  var getName = function() {
    return name;             // 내부 함수는 외장 함수의 'name' 변수에 접근 할 수 있습니다.
  }
  return getName;            // 내부 함수가 리턴함으로써, 외부 함수로 노출됩니다.
},
myPet = pet("Vivie");
   
myPet();                     // "Vivie"로 리턴합니다.
```

# File I/O
https://msdn.microsoft.com/ko-kr/library/k3352a4t(v=vs.110).aspx
https://kldp.org/node/152110


- 참고로 보고 정리할 링크
https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration#레이블_문 
레이블문
https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration
루프와 반복
https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/%ED%95%A8%EC%88%98
https://developer.mozilla.org/ko/docs/A_re-introduction_to_JavaScript
https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/%ED%95%A8%EC%88%98
함수
http://emflant.tistory.com/66
내장함수와 클로


