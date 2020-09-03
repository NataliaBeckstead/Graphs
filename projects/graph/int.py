

def sum_of_val(dic):
    sum = 0
    for val in dic.values():
        if type(val) == int:
            sum += val
    return sum

print(sum_of_val({
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}))