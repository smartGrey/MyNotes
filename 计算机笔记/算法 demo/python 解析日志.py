import re
a = '2022-05-19 13:15:13.715 [xxx] [xx] []  [rig[]h[]t]  []   [aaa]  []'
result = re.match(r'^.*\[.*\].*\[.*\].*\[.*\].*\[(.*)\].*\[.*\].*\[.*\].*\[.*\]$', a)
# print(result.group(0))
print(dir(result))
# print(result.groupdict())
print(result.string)




def get_nth_part(str, n):
  result = []
  level = 0
  level_1_time = 0
  for c in str:
    if c=='[':
      level+=1
      if level==1: level_1_time+=1
    elif c==']':
      level-=1
    if 0<level and level_1_time==n:
      result.append(c)
  return ''.join(result[1:]) if level==0 else 'error'

print(get_nth_part('2022-05-19 13:15:13.715 [xxx] [xx] []  [rig[]h[]t]  []   [aaa]  []', 4))# 'rig[]h[]t'
print(get_nth_part('2022-05-19 13:15:13.715 [xxx] [xx] []  [rig[]h[[]t]  []   [aaa]  []', 4))# 'error'
