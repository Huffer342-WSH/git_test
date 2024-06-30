def sub(a, b):
    """
    计算两个元素的差。这两个元素可以是数字或数字列表。
    
    参数:
    a -- 第一个元素，可以是整数、浮点数或整数列表。
    b -- 第二个元素，可以是整数、浮点数或整数列表。
    
    返回值:
    两个元素的差，如果输入是数字，则返回数字之差；
    如果输入是列表，则返回对应元素相减后的列表。
    
    抛出异常:
    TypeError -- 如果输入的参数类型不正确（既不是数字也不是列表）。
    ValueError -- 如果两个列表的长度不相等。
    """
    # 如果 a 和 b 都是数字，直接相减
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    
    # 如果 a 和 b 都是列表，逐元素相减
    elif isinstance(a, list) and isinstance(b, list):
        # 检查列表长度是否相等
        if len(a) != len(b):
            raise ValueError("The lists must be of the same length")
        return [x - y for x, y in zip(a, b)]
    
    # 如果 a 是列表，b 是数字
    elif isinstance(a, list) and isinstance(b, (int, float)):
        return [x - b for x in a]
    
    # 如果 a 是数字，b 是列表
    elif isinstance(a, (int, float)) and isinstance(b, list):
        return [a - y for y in b]
    
    else:
        raise TypeError("Both arguments must be either numbers or lists")
