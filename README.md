# korean-mcfaq
국립국어원 온라인가나다 상담 사례 모음 자주 묻는 질문 크롤링

ray를 활용하여 병렬 수집으로 빠르게 얻을 수 있다.

# 필요한 패키지

```python
pip install pandas requests lxml ray
```

# 데이터

![image](https://github.com/HaloKim/korean-mcfaq/assets/44603549/1823cfab-2cd9-4c1c-9451-befb40b8ee34)

# 후처리

```python
import re

df[['질문', '답변']] = df[['질문', '답변']].apply(lambda x: x.apply(lambda y: re.sub('\n|\t|\r', '', y).strip()))
```

![image](https://github.com/HaloKim/korean-mcfaq/assets/44603549/87d97b05-97b7-4a50-ab95-335f533428cf)


# 참조

[온라인가나다 상담 사례 모음](https://korean.go.kr/front/mcfaq/mcfaqList.do?mn_id=217)

[ray](https://www.ray.io/)
