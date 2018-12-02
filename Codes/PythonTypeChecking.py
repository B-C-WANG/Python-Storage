
import numpy as np

'''
python的静态类型检查，似乎只相当于注释，只能够让ide提示，运行时无限制

'''

def string_to_int_trans(a:str) -> int:
    return int(a)

def get_element_in_numpy(array:np.ndarray) -> float:
    return float(array[0])
class ABC():
    def __str__(self) -> str:
        return "1"

def from_class_to_string(abc:ABC) -> str:
    return str(abc)


print(get_element_in_numpy([0]))
print(from_class_to_string(ABC()))


