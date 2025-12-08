import math

_file = open("input.txt", "r")
_ranges = _file.read().replace("\n","").split(",")
_sum = 0
for _range in _ranges:
    _borders = _range.split("-")
    _start = int(_borders[0])
    _end = int(_borders[1])

    for _number in range(_start, _end + 1):
        _s_number = str(_number)
        _lenght = len(_s_number)
        if _lenght > 1:
            for _denominator in range(1,math.floor(_lenght/2) + 1):
                if _lenght % _denominator == 0:
                    _sub_numbers = []
                    for _part in range(0,int(_lenght/_denominator)):
                        _sub_numbers.append(_s_number[_part * _denominator:(_part * _denominator) + _denominator])
                    if len(set(_sub_numbers)) == 1:
                        _sum += _number
                        break
print(_sum)