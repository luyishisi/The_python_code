import subprocess
import time

frames = 10

for i in range(1,frames):
    filename = "test"+format(i,"03d") + ".jpg"
    subprocess.call(["raspistill", "-n", "-t", "1", "-w",
        "200", "-h", "200", "-co", "90", "-ifx", "sketch",
        "-e", "jpg", "-0", filename])
    print ("taking photo",i)

print("Encoding....")
subprocess.call(["avconv"," -
