# 테스트 코드 기본 개념

### 1. 테스트 코드와 실제 코드는 의존성 관계가 아니다.
(통합 테스트의 경우) 테스트 config를 통해 실제 app을 띄우기 때문에
로직이 담긴 실제 코드로 app을 띄운 것과 마찬가지이다.

### 2. 실제 코드가 변경됐을 때, 테스트 코드를 통해서 버그를 잡을 수 있다.
의존성 관계가 아니지만 테스트 코드와 실제 코드는 동일하게 app을 바라보고 있고,
테스트 코드는 세부 로직을 검사하는 것이 아니라 결과 값만 확인하는 것이므로 버그를 잡아낼 수 있다.
예컨대, 세부 로직을 바꾼 후에도 200 응답이 뜬다면 우리가 바라던 결과는 얻어진 것이고,
200 응답을 받을 수 있던 것이 400, 500대 응답을 받는다면 세부 로직이 잘못됐음을 알 수 있다.

### 3. 위와 같은 이유로 테스트 코드는 포스트맨을 대신할 수 있다.

### 4. Unit test와 통합 테스트는 다르다.
Unit test는 특정 함수, 메소드가 올바르게 작동하는지 보는 보다 간편한 테스트를 말한다.
예를 들면 더하기 함수가 1+2 == 3 을 맞게 계산하는지 확인하는 테스트가 있다.
반면 통합 테스트는 실제 app을 띄워서 로직이 잘 작동하는지를 보는 것이므로 규모면에서 훨씬 크다고 할 수 있다.

$$$ 5. 테스트 코드는 무조건 Given/ When/ Then 규칙에 의해 작성해야 한다.
- Given: 가지고 있는 값들
- When: 내가 취할 액션
- Then: 기대하는 결과