import subprocess
print("Intruduzca la ip Objetivo")
target = input()
print("Objetivo" , target)
print("Iniciamos filtrando los puertos abiertos")
subprocess.run(["nmap", "-p-", "--open", "-sS", "--min-rate","5000", "-vvv", "-n", target , "-oG", "PuertoAbiertos"])
print("Ahora Analizaremos las vulnerabilidades")
subprocess.run(["nmap", "-v" ,"-sS" "vulnerabilidades.xml" , "--stylesheet=https://svn.nmap.org/nmap/docs/nmap.xsl", "--script=vuln", target])
