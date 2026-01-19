from subprocess import Popen, PIPE

text = open('test01.html',encoding='utf-8').read()
tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)

tidy.stdin.write(text.encode())
tidy.stdin.close()

print(tidy.stdout.read().decode())