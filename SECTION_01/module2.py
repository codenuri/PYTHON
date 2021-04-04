# 1. print() 함수는 built in function 이므로 어떤 모듈도 필요 없습니다.
print('Hello, Python')


# 2. os 모듈을 사용하면 터미널(콘솔)창의 기본 명령을 실행할수 있습니다.
import os
os.mkdir('E:\\PYTHON_TEST')


# 3. shutil 모듈에는 파일 관련 함수를 제공합니다.
import shutil
shutil.copyfile('C:\\Windows\\system32\\calc.exe', 'E:\\PYTHON_TEST\\a.exe')

# 4. random 모듈에는 난수 관련 다양한 함수를 제공합니다.
import random
r1 = random.random()        # 0 ~ 1.0
r2 = random.uniform(1,100)  # first ~ last


# 5. 프로그램을 실행하려면 subprocess 모듈을 사용하면 됩니다.
import subprocess
completed = subprocess.run(['calc.exe'])

# https://docs.python.org/ko/3/library/index.html  참고

