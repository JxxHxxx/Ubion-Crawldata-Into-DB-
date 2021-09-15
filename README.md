# Ubion-Crawldata-Into-DB-

info

1. int 는 컴마(,)를 인지하지 못한다. replace 를 통해 , 를 없애자.
2. find_all 은 텍스트로 반환하기 힘들다. 반복문을 통해 string 으로 만들자.
3. 현재 짜놓은 코드는 매우 메모리를 많이 잡아먹는 방법이다.
4. db 는 분명 key, value 구조임에 틀림없다. 한 행씩 import 하는 것보다. key, value 에 맞춰 열단위로 데이터를 import 하는게 빠르다고 생각한다.
5. 그 이유는 parquet 구조를 보면 알 수 있다. 물론 아닐수도 있다. 내 뇌피셜일 뿐, 시도는 집에가서 하자
