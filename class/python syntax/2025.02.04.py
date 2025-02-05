# 상속

class plus_minus:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def plus(self):
        result = self.first + self.second
        return result
    def minus(self):
        result = self.first - self.second
        return result

class MoreFunction(plus_minus):
    def __init__(self, first, second,third):
        super().__init__(first, second)
        self.third = third
    def mul(self):
        result = self.first*self.second*self.third
        return result
    # 메소드 오버라이딩
    def plus(self):
        result = self.first + self.second + self.third
        if result > 100:
            return "버그"
        else:
            return result
    # super() 활용, 부모클래스의 plus 함수 가져오기
    def parents_plus(self):
        ret = super().plus()
        return ret

# 자식클래스의 인스턴스로 부모클래스의 메소드에 접근 가능함.
b = MoreFunction(3,4,5)
print(b.mul())
print(b.plus())
print(b.minus())

# 부모클래스의 plus 메소드를 자식클래스에서 수정하려고함
# plus 메소드에서 숫자 2개가 아닌 3개의 합을 출력하는 메소드로 바꾸고,
# 만약에 숫자의 합이 100이 넘는다면 '버그'라고 출력이 되도록 수정해보기
a = MoreFunction(1,1,999)
print(a.plus())
print(a.parents_plus())

# 메소드 오버로딩 vs 메소드 오버라이딩
# 메소드 오버로딩 = 클래스 내의 동일한 이름의 메소드가 여러개 존재하는 것, 파이썬에선 미구현, 다른 인자 개수 또는 다른 타입의 인자 입력받기 등
# 다형성 : 동일한 메소드가 클래스에 따라 다르게 행동할 수 있다는 뜻. ex) 메소드 오버라이딩
# 상속 : 자식클래스가 부모클래스로부터 메소드 또는 속성 등을 물려받아 사용하는 것.
# 추상화 : 객체들의 공통된 속성이나 기능을 묶어 상위클래스에 구현하고, 하위클래스에는 각각 개체의 고유기능만 추가하는 것.
# 캡슐화 : 클래스 내 객체(속성 또는 메소드)를 외부에서 수정하지 못하도록 막는 것. 
# public = 우리가 평소 사용하는 코드
# protected = "암묵적 규칙 (_)"에 의해 메소드를 호출시 부모클래스 내부나 자식클래스에서만 호출되도록 하는 것, 바로 호출이 가능은 함.
# private = __ 규칙에 의해 클래스에 의해서만 호출이 가능함. 바로 호출은 불가능.
# getter 데코레이터는 private한 변수 값을 읽을 목적으로 만든 것.    @property 
# setter 데코레이터는 private한 변수 값을 변경할 목적으로 만든 것.  @함수명.setter

