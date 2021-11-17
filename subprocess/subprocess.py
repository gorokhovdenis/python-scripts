import subprocess
with open('./vips.txt', 'r') as f1:
     for line in f1:
        try:
            s=str(subprocess.check_output('curl -m 5 -sSI https://'+line.split("\n")[0]+' | grep Strict-Transport-Security', shell=True))
            if "Strict" in s:
                print ('HSTS enabled in '+line.split("\n")[0])
        except Exception:
            pass
            