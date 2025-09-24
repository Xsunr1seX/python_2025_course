import tokenize
import io


# 1) этап 1 - токенизация кода на языке пайтон
code = "x = 5 + 3"
#tokens = tokenize.generate_tokens(io.StringIO(code).readline)
#for tok in tokens:
#    print(tok)

# 1) этап 2 - построение абстрактного синтаксического дерева(АSТ)
#import ast #библиотека которая позволяет построить ситнаксическое бинарное дерево, которое будет переводится в байт-код

#tree = ast.parse(code)
#print(*ast.dump(tree, indent=2)) #компилятор не волшебный, он считывает не по строкам.

# 3) этап 3 - компиляция в байт код

import dis

def greet():
    print("Hello!")

dis.dis(greet)

# 4) этап 4 - запуск на PVM
# запускается бинарник из шага 3 ( бинарники можно найти в __pychache__ папке)

# вопрос на подумать - как добавляются сторонние модули на питоне?

