import pandas as pd

# 간단한 매출 데이터
data = {
    "요일": ["월", "화", "수", "목", "금", "토", "일"],
    "매출": [100, 120, 130, 115, 140, 200, 220]
}

df = pd.DataFrame(data)

# 요일별 매출 확인
print(df)

# 평균 매출
print("평균 매출:", df["매출"].mean())

# 최대 매출 요일
max_day = df.loc[df["매출"].idxmax(), "요일"]
print("최대 매출 요일:", max_day)