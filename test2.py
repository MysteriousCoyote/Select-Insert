import subprocess
#subprocess.run(["ls", "-l"] )

#subprocess.run("echo Hello")

t = subprocess.Popen("docker inspect --format '{{ .NetworkSettings.IPAddress }}' zookeeper", shell=True, stdout=subprocess.PIPE).stdout.read()

for i in t:
    print(i)

print(t)
