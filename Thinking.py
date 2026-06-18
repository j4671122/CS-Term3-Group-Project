# 1번째 줄 주석: [본인 이름(첫 이니셜+성)] & [파트너 이름(첫 이니셜+성)] (예: J. Jonker, S. Jonker)

class Student:
    """
    학생 개별의 정보(이름, 학년, 성적)를 관리하고 
    개인 통계를 계산하는 클래스
    """
    def __init__(self, student_name: str, year_group: int, raw_grades: dict):
        # 인스턴스 생성 시 모든 식별 정보와 raw_grades 딕셔너리를 저장
        self.name = student_name
        self.year_group = year_group  # 9, 10, 11, 12 중 하나
        self.grades = raw_grades      # 예: {'Math': [55, 60, 77], ...}

    def subjectavg(self, subjectname: str) -> float:
        """특정 과목(subjectname)의 3개 학기 평균 점수를 계산하여 반환"""
        # TODO: self.grades[subjectname] 리스트의 평균을 구해 리턴하세요.
        pass

    def yearavg(self) -> float:
        """모든 과목의 전체 학기 평균 점수를 계산하여 반환"""
        # TODO: 모든 과목의 평균들을 모아서 최종 올해 총평균을 리턴하세요.
        pass

    def failcheck(self) -> bool:
        """특정 과목의 평균이 55점 미만인 경우 낙제 메시지를 출력하고 결과를 반환"""
        # TODO: subjectavg를 활용해 하나라도 55점 미만인지 체크하고 print문으로 알리세요.
        pass

    def writegrades(self, target_dictionary: dict):
        """지정된 딕셔너리에 이 학생의 과목별 평균과 올해 전체 평균 정보를 저장"""
        # TODO: target_dictionary에 self.name을 키로 하여 통계 데이터를 저장하세요.
        pass


# =====================================================================
# 메인 프로그램 영역 (Main Program)
# =====================================================================

# 1. 4명 이상의 샘플 데이터 준비 (테스트 케이스용 데이터)
# 과제 조건: 이름은 유일해야 하며, 과목은 Math, Science, English 고정
student_data_sample = {
    "Alice": {"year": 11, "scores": {'Math': [85, 90, 80], 'Science': [92, 95, 89], 'English': [78, 82, 80]}},
    "Bob": {"year": 10, "scores": {'Math': [50, 52, 54], 'Science': [70, 65, 72], 'English': [60, 58, 62]}},
    "Charlie": {"year": 12, "scores": {'Math': [95, 97, 96], 'Science': [90, 92, 94], 'English': [88, 91, 90]}},
    "David": {"year": 9, "scores": {'Math': [70, 75, 72], 'Science': [50, 55, 48], 'English': [65, 68, 70]}}
}

# 2. Student 클래스의 인스턴스들을 담을 리스트 또는 딕셔너리 생성
student_instances = []
for name, info in student_data_sample.items():
    # 각 학생별로 Student 인스턴스를 동적으로 생성하여 리스트에 추가
    student_obj = Student(name, info["year"], info["scores"])
    student_instances.append(student_obj)

# 3. 요구사항 1: 모든 학생 정보를 알파벳 순서로 정렬 및 출력
print("--- [1] 학생 정보 (알파벳순 정렬) ---")
# TODO: student_instances를 학생 이름(student_obj.name) 기준으로 정렬 후 반복문으로 출력하세요.


# 4. 요구사항 2: 각 학생의 낙제 여부 확인 및 메시지 출력 (failcheck 메서드 활용)
print("\n--- [2] 과목 낙제 여부 확인 (기준: 평균 55점 미만) ---")
# TODO: 반복문을 돌며 각 학생 인스턴스의 failcheck()를 실행하세요.


# 5. 요구사항 3: 올해의 최고 평균 득점자 찾기 (동점자 처리 필수)
print("\n--- [3] 올해 최고 총평균 학생 ---")
# TODO: 모든 학생의 yearavg()를 비교하여 가장 높은 학생(들)을 찾아 출력하세요.


# 6. 요구사항 4: 가장 어려운 과목 찾기 (전체 학생 기준 가장 낮은 평균 점수, 동점 과목 처리 필수)
print("\n--- [4] 가장 어려운 과목 ---")
# TODO: Math, Science, English 각각의 전체 학생 평균을 구해 가장 낮은 과목을 출력하세요.