## 상황: 1,2,3차 시험이 있는데 전 단계에 불합격하면 이후 단계는 합격/불합격을 개별적으로 관리자가 선택하지 않아도 되도록 모두 불합격 처리 하기
> 조건문 쿼리를 검색했을 때 case문 나오는 것을 보고 이대로 짜보려고 함
> 중첩을 어떻게 처리해야 할지 모르겠고 무튼 엄청 더럽고 이해하기 어려움

```sql
// table 구조
// rid | reg_id | name | DOB | gender | email | phone | curriculum | education | major | experience | introduction 
// | graduation_certificate | grade_certificate | experience_certificate1 | experience_certificate2 | register_date 
// | register_ip | stage1_pass | stage1_pass_date | stage2_pass | stage2_pass_date | stage3_pass | stage3_pass_date 
// | curriculum2 | etc_document | modify_date | modify_ip | undergrad_school | undergrad_major | undergrad_status 
// | grad_school | grad_major | grad_status | grad_course | final_student

UPDATE '.REG_TABLE.'
    // 1차 불합격했다 -> 2,3차 자동으로 불합격 표시 + 결정된 시간도 같이 표시
    // 1차 합격 + 2차 불합격 -> 3차 자동으로 불합격 표시 + 결정된 시간도 같이 표시
    // 3차만 불합격 -> 3차에만 불합격 표시 + 결정된 시간도 같이 표시
    
    
    // 3차 합격,불합격 여부 (Y/N)을 수정하려고 함
	SET '.stage3_pass.' = 
	    // 2차가 불합격했을 경우 (N)
		CASE WHEN '.stage2_pass.' = '.N.'
		      // 1차도 불합격했는지 다시 확인하고
		      THEN CASE WHEN '.stage1_pass.' = '.N.'
		                // 그렇다면 3차도 확실히 불합격 값으로 채움
                        THEN '.N.'
                        // *** 그리고 이때! 합격, 불합격 여부 결정난 time도 다시 now()로 하고 싶다
                        // 기타 경우에는 3차 원래 값 그대로 가지고 있어라
                        ELSE '.stage3_pass.' END,
    // 2차 합격, 불합격 여부 수정
    SET '.stage2_pass.' = 
        // 1차 불합격했다면
        CASE WHEN '.stage1_pass.' = '.N.'
              // 2차는 불합격 값으로 채움
              THEN '.N.' 
              // ** 그런데 이때 3차도 자동으로 불합격 값으로 채워야 하는데 어떻게 중첩하지?
              // ** 2,3차 중첩해서 다 불합격 채우고 나서 time도 다시 now()
              ELSE '.stage2_pass.' END,
WHERE reg_id = "'.$conn->escape_string($reg_id).'"
```

## 해결1. 단순하게 경우대로 각각 update한다
> 단순하게 생각하면 이렇게 손쉽게 해결했을텐데 어렵게만 생각했다 (조언 감사 ㅠㅠ)
> 1차를 불합격했고 2차, 3차가 빈 값이면 모두 불합격 처리 (처음부터 떨어진 경우)
```sql
update moel_registrations 
set stage2_pass = 'N', stage2_pass_date = NOW(), stage3_pass = 'N', stage3_pass_date = NOW()  
where stage1_pass = 'N'
and stage2_pass = ''
and stage3_pass = '';

```
> 2차를 불합격했고 3차가 빈 값이면 3차만 불합격 처리 (1차는 붙었는데 2차에서 떨어진 경우)
```sql
update moel_registrations 
set stage3_pass = 'N', stage3_pass_date = NOW()  
where stage2_pass = 'N'
and stage3_pass = '';
```

## 해결2. 프로시저를 만들어서 해보세요 (공부해야 하는 부분)
> 너무 답답해서 sqler 사이트에 질문을 했다, 그랬더니 조언해주시면서 알려주신 것 ㅠㅠㅠ (천사)
```sql
update REG_TABLE set stage1_pass='값' where reg_id = "'.$conn->escape_string($reg_id).'"

if(select stage1_pass from reg_table WHERE reg_id = "'.$conn->escape_string($reg_id).'" = 'N')
begin
	update reg_table 
set	stage2_pass = 'N', stage3_pass = 'N'
WHERE reg_id = "'.$conn->escape_string($reg_id).'"
end 
```
