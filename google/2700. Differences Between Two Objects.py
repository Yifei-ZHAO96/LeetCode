# DFS O(N) O(N)
def obj_diff(obj1, obj2):
    if type(obj1) != type(obj2):
        return [obj1, obj2]
    
    if not isinstance(obj1, dict):
        return {} if obj1 == obj2 else [obj1, obj2]

    result = {}
    
    for k, o1 in obj1.items():
        if k not in obj2:
            continue
        
        o2 = obj2[k]
        if isinstance(o1, dict) and isinstance(o2, dict):
            sub_diff = obj_diff(o1, o2)
            if sub_diff:
                result[k] = sub_diff
        elif isinstance(o1, list) and isinstance(o2, list):
            sub_diff = obj_diff_list(o1, o2)
            if sub_diff:
                result[k] = sub_diff
        elif o1 != o2:
            result[k] = [o1, o2]
    
    return result

def obj_diff_list(list1, list2):
    min_len = min(len(list1), len(list2))
    result = {}
    
    for i in range(min_len):
        o1 = list1[i]
        o2 = list2[i]
        if isinstance(o1, dict) and isinstance(o2, dict):
            sub_diff = obj_diff(o1, o2)
            if sub_diff:
                result[i] = sub_diff
        elif isinstance(o1, list) and isinstance(o2, list):
            sub_diff = obj_diff_list(o1, o2)
            if sub_diff:
                result[i] = sub_diff
        elif o1 != o2:
            result[i] = [o1, o2]
    
    return result


obj1 = {
  "a": 5, 
  "v": 6, 
  "z": [1, 2, 4, [2, 5, 7]]
}
obj2 = {
  "a": 5, 
  "v": 7, 
  "z": [1, 2, 3, [1]]
}

output = {
  "v": [6, 7],
  "z": {
    "2": [4, 3],
    "3": {
      "0": [2, 1]
    }
  }
}
print(obj_diff(obj1, obj2))

obj1 = {}
obj2 = {
  "a": 1, 
  "b": 2
}
Output = {}
print(obj_diff(obj1, obj2))

obj1 = {
  "a": 1,
  "v": 3,
  "x": [],
  "z": {
    "a": None
  }
}
obj2 = {
  "a": 2,
  "v": 4,
  "x": [],
  "z": {
    "a": 2
  }
}
Output = {
  "a": [1, 2],
  "v": [3, 4],
  "z": {
    "a": [None, 2]
  }
}
print(obj_diff(obj1, obj2))

obj1 = {
  "a": {"b": 1}, 
}
obj2 = {
  "a": [5],
}
Output = {
  "a": [{"b": 1}, [5]]
}
print(obj_diff(obj1, obj2))

obj1 = {
  "a": [1, 2, {}], 
  "b": False
}
obj2 = {   
  "b": False,
  "a": [1, 2, {}]
}
Output = {}
print(obj_diff(obj1, obj2))