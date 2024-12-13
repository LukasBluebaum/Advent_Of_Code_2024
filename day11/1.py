with open("in.txt") as f:
  nums = f.readlines()[0].strip().split(" ")
  nums = [int(n) for n in nums]

for _ in range(25):
  new = []
  for n in nums:
    s = str(n)
    if n == 0:
      new.append(1)
    elif len(s) % 2 == 0:
      new.append(int(s[:len(s)//2]))
      new.append(int(s[len(s)//2:]))
    else:
      new.append(n * 2024)
  nums = new
print(len(nums))

