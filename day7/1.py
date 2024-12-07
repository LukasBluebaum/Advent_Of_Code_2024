with open("in.txt") as f:
  lines = f.readlines()


def test(i, nums, target, current, dp):
  if i == len(nums):
    return target == current
  if current > target:
    return False
  if (i, current) in dp:
    return dp[(i, current)]

  plus = test(i+1, nums, target, current + nums[i], dp)
  mult = test(i+1, nums, target, current * nums[i] if i > 0 else nums[i], dp)
  dp[(i, current)] = plus or mult
  return dp[(i, current)]

res = 0
for line in lines:
  target, nums = line.split(":")
  target = int(target)
  nums = [int(n) for n in nums.split(" ")[1:]]
  if test(0, nums, target, 0, {}):
    res += target
print(res)
