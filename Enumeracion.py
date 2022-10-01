import subprocess
print("Enter the target ip")
target = input()
print("Target" , target)
print("Filtering open ports")
subprocess.run(["nmap", "-p-", "--open", "-sS", "--min-rate","5000", "-vvv", "-n", target , "-oG", "Open Ports"])
print("Ahora Analizaremos las vulnerabilidades")
subprocess.run(["nmap", "-v" ,"-sS","vulnerabilidades.xml" , "--stylesheet=https://svn.nmap.org/nmap/docs/nmap.xsl", "--script=vuln", target])
