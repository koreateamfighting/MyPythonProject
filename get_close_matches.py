# 유사도 관련 알고리즘
from difflib import get_close_matches

#word = 'Opening the window.'
word = '말씀하세요.'

candidates = ['네 말씀하세요.','말씀하세요','다시 말씀해주세요.','말씀하세요.']
#candidates = ['Opening the windows.','Opening all windows.','Openning the driver`s window','Opening the trunk','Opening the window.']
n = 3
cutoff = 0.7

close_matches = get_close_matches(word,candidates,n,cutoff)

print(close_matches)
