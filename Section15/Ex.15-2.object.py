class Calculator:
    def input_expr(self):
        expr = input('수식을 입력하세요 >>')
        self.expr = expr

    def calculate(self):
        return eval(self.expr)

calc= Calculator()
calc.input_expr()
print('수식결과는 45입니다')