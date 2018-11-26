### 클로저
이미 생명 주기가 끝난 외부 함수의 변수(자유 변수)를 참조하는 함수  
주로 내부 함수를 리턴하는 외부 함수의 조합으로 만들어지는 경우가 많음.

### 클로저 활용 예시
1. 특정 함수에 사용자가 정의한 객체에 메서드 연결
```javascript
function HelloFunc(func) {
    this.greetiing = 'hello';
}

HelloFunc.prototype.call = function(func) {
    func ? func(this.greeting) : this.func(this.greeting);
}

var userFunc = function(greeting) {
    console.log(greeting);
}

var objHello = new HelloFunc();
objHello.func = userFunc;
objHello.call();
```
```javascript
function saySomething(obj, methodName, name) {
    // 매개 변수들 -> 자유 변수
    // 반환되는 아래 함수 -> 클로저
    return (function(greeting) {
        return obj[methodName](greeting, name);
    })
}

function newObj(obj, name) {
    obj.func = saySomething(this, 'who', name);
    return obj;
}

newObj.prototype.who = function(greeting, name) {
    console.log(greeting + " " + (name||'everyone'));
}
```

[출처] 인사이드 자바스크립트