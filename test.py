def calculate_average_frequency():
    total_incidents = int(input("총 발생 횟수를 입력하세요: "))
    survey_period = int(input("조사 기간 (연 단위)을 입력하세요: "))
    average_frequency = total_incidents / survey_period
    return average_frequency
afr = calculate_average_frequency()
print(f"평균 재해 빈도는 {afr} 입니다.")
