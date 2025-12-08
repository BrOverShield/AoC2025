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
        if _lenght % 2 == 0: #if the number has a pair amount of digits
            _middle = int(_lenght / 2)
            _first_half = _s_number[:_middle]
            _second_half = _s_number[_middle:]
            if _first_half == _second_half:
                _sum += _number
print(_sum)
            
                    