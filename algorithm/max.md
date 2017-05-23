# 1. 두 값 중 큰 값을 구하는 함수 (max2) 작성하시오.
> Function max2(a,b){}  
> max2(1,2)===2
```javascript
function max2(a, b){
	return a > b ? a : b;
}
```

# 2. 세 값 중 큰 값을 구하는 함수(max3)을 작성하시오.
> Function max3(a,b,c){}  
> max3(1,2,3)===3
```javascript
function max3(a,b,c){
    var max = 0;
	for(var i = 0; i < 3; i++){
		if (a>max) {
             max = a;
         } else if (b>max) {
             max = b;
         } else { // 몇몇 경우 오류 ㅠㅠ 
         // else if (c>max) 조건으로 수정해야!
             max = c;
         }
 	}
 	return max;
 };
```

```js
// 간편한 풀이
function max3(a,b,c){
    return a >b ? a : b > c ? b : c;
 }
```

# 3. n개의 인자를 받아 가장 큰 값을 구하는 함수(maxN)을 작성하시오.
> Function maxN(){}
```javascript
function maxN(arr){
    var max = 0;
 	for (var i=0; i<arr.length; i++){
 		if(arr[i]>max){
 			max = arr[i]
 		}
 	}
 	return max;
 }
```

```javascript
// mdn 풀이 참고
function max(...arr) {
	return arr.reduce((a,b) => a > b ? a : b);
}
function max(...arr) {
 	return arr.reduce((a,b) => Math.max(a, b));
}
function max(...arr) {
	return Math.max(...arr);
}
```

# 4. 1부터 N까지 합을 구하는 함수를 작성하시오.
> Function sumN(n){}  
> sumN(10) === 55
```javascript
function sumN(n){
 	var sum = 0;
 	for(var i = n; i >= 1; i--){
 		sum += i;
 	}
 	return sum;
 }
```

# 5. 패스워드 유효성 검사하는 함수를 작성하시오. (8자 이상, 하나 이상 숫자 포함, 하나 이상 영문자 포함)
> Function validate(password){}  
> validate(“1234567”) === false validate(“1234567a”) === true
- 정규식 활용: d = 숫자 의미함
```javascript
function validate(password) {
	return !!password 
			&& !!password.match(/\d/) 
			&& !!password.match(/[a-zA-Z]/)
			&& password.length >= 8;
}
```