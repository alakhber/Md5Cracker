import itertools                                                  
import hashlib                                                    
import sys                                                        
import time                                                       
import os                                                         
print"#######################################################"    
print"#                                                     #"    
print"#     ____                          _         _       #"    
print"#    |  _ \    ___   _ __  __   __ (_)  ___  | |__    #"    
print"#    | | | |  / _ \ | \"__| \ \ / / | | / __| | \"_ \   #"  
print"#    | |_| | |  __/ | |     \ V /  | | \__ \ | | | |  #"
print"#    |____/   \___| |_|      \_/   |_| |___/ |_| |_|  #"
print"#                                                     #"
print"#                                                     #"
print"#                              Md5 Cracker v.1        #"
print"#######################################################\n"                     
print "1 - Haqqinda "
print "2 - Istifade Qaydasi"
print "3 - Istifade "


inp = raw_input("Input > ") # Istifadeciden Secim Alma
if inp == '1':                                                                         
    os.system("clear")
    print"\n############################################################## "       
    print"# Muellif Huquqlarini Pozmag Qeti Qadagandir !  "
    print"# Elaqe Ucun Facebook Adress: fb.com/alakber  "
    print"# Mail  : dead-nick@mail.ru "
    print"# Gmail : nakhiyev.alakhber@gmail.com   "                                
    print"##############################################################\n"
if inp == '2':
    os.system("clear")
    print"\n##############################################################"
    print"# Md5 Daxil Edin: Qirilacag Olan Md5 Daxil Edin"                 
    print"# Interfs Gosterilsin (Default Y) [H/Y] ? : Y"
    print"# H - Programa Sade Interfesy Daxil Edir.Programi Lengidir"      
    print"# Y - Programa Interfeys Daxil Etmir.Programi Suretlendirir"     
    print"################################################################\n"
if inp == '3':                                                               
    os.system("clear")
    print"##############################################################"            
    passwords = raw_input("# Md5 Daxil Edin: ")                                      # Md5-i Istifadecidn Alma
    if 16 == int(len(passwords)) or 32 == int(len(passwords)):                       # Md5-in uzunlugunu Yoxlama (md5 shifrelerin uzunlugu 16 ve 32 Olur )
        interfeys = raw_input("# Interfs Gosterilsin (Default Y) [H/Y] ? : ")        # Istifadeciden Interfeys Alma (Program Isleyerken Ekranda yoxlanan shifrelerin gorsenib gorsenmemesi)
        print"##############################################################\n"      # Makyaj
        os.system("clear")
        m = ["-", "\\", "|", "/"]
        chrs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_*!@?|^&+<>#{}[];:%()\'");'
        n = 100
        j = 0
        time_bas = time.time()
        for i in range(1, n):
            for xs in itertools.product(chrs, repeat=i):
                kod = ''.join(xs)
                # print md5.md5(kod).hexdigest()
                if interfeys == 'h' or interfeys == 'H':
                    if passwords == hashlib.md5(kod).hexdigest():
                        os.system("clear")
                        time_son = time.time()
                        print "Cracked : "+passwords+" ==> "+kod
                        end_time = time_son-time_bas
                        # print "Stop: "+"%.6s" %str(end_time)+" sec"
                        # print "Stoped  : "+str(end_time)+" sec"
                        quit()
                    sim = m[j]
                    # sys.stdout.write(kod+"\r")
                    sys.stdout.write("Cracking ... "+sim + "\r")
                    sys.stdout.flush()
                    time.sleep(0.00000001)
                    del (kod)
                elif interfeys == 'y' or interfeys == 'Y':
                    if passwords == hashlib.md5(kod).hexdigest():
                        os.system("clear")
                        time_son = time.time()
                        print "Cracked : "+passwords+" ==> "+kod
                        end_time = time_son-time_bas
                        #print "Stop: "+"%.6s" %str(end_time)+" sec"                     #
                        # print "Stoped  : "+str(end_time)+" sec"
                        quit()
                if j == 3:
                    j = 0
                j = j+1
    else:                                                                            # Md5 duzgun olmadiqda
        print"# Md5-in Duzgun Oldugundan Emin Olun "                                 # Makyaj
        print"##############################################################\n"      # Makyaj
        quit()
