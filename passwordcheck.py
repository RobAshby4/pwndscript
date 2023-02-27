import requests
import sys
import hashlib

def get_hashes(pwh):
    url = "https://api.pwnedpasswords.com/range/" + pwh[:5]
    res = requests.get(url)
    return res.text

def hashpwds(pw):
    hashedpw = []
    for password in pw:
        hashedpw.append(hashlib.sha1(password.encode()).hexdigest())
        hashedpw[-1] = hashedpw[-1].upper()
    return hashedpw

def main():
    if len(sys.argv) < 2:
        print("Please provide a file containing passwords as an argument")
        return
    filename = sys.argv[1]
    fp = None
    try:
        fp = open(filename)
    except:
        print("invalid filename, does " + sys.argv[1] + " exist?")
        return
  
    pw = fp.readlines()
    for i in range(0, len(pw)):
        pw[i] = pw[i].strip()
   
    hashedpw = hashpwds(pw)
        
    for i in range(0, len(pw)):
        if len(pw[i]) < 1:
            continue
        res = get_hashes(hashedpw[i])
        if hashedpw[i][5:] in res:
            print("Pwnd: " + pw[i])
        else:
            print("Not-Pwnd: " + pw[i])
            

if __name__ == "__main__":
    main()

