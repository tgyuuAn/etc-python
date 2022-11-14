class student_score:
    def __init__(self, name, id_number, kor_score, math_score, eng_score):
        self.name = name
        self.id_number = id_number
        self.__score_list = [kor_score,math_score,eng_score]
        
    def __str__(self):
        return f"{self.name}({self.id_number})의 국영수 점수를 저장합니다."
    
    def get_score(self):
        return self.__score_list
    
    def set_score(self, new_kor, new_math, new_eng):
        if new_kor >= 0 and new_math >= 0 and new_eng:
            self.__score_list[0] = new_kor
        else :
            raise ValueError("양의 실수를 입력하세요")
    def get_avg_score(self):
        return sum(self.__score_list)/3
    
student_1 = student_score("Tae-Gyu An", 201912047, 40, 50, 90)
student_2 = student_score("Ji-San Kim", 201911589, 80, 90, 100)
student_3 = student_score("Jun-Pyo Hong", 202011234, 100, 100, 100)
student_1.set_score(10,20,30)
print(f"{student_1.name}({student_1.id_number})의 국영수 성적 : {student_1.get_score()[0]}, {student_1.get_score()[1]}, {student_1.get_score()[2]}")
print(f"{student_1.name}({student_1.id_number})의 평균성적 : {student_1.get_avg_score()}")
print(f"{student_2.name}({student_2.id_number})의 평균성적 : {student_2.get_avg_score()}")
print(f"{student_3.name}({student_3.id_number})의 평균성적 : {student_3.get_avg_score()}")