import urllib
main_url = "http://www.promacedonia.org/bmark/gp/gal/"

#for n in range(346,404):
#    urllib.urlretrieve (main_url+"p_0"+str(n)+".jpg", "./Parlichev/p_0"+str(n)+".jpg")

name_list = ["p_000_koritsa",
"p_000_sydyrzhanie_1",
"p_000_sydyrzhanie_2",
"p_000_sydyrzhanie_3",
"p_000_sydyrzhanie_4"]

for name in name_list:
    urllib.urlretrieve (main_url+name+".jpg", "./Parlichev/"+name+".jpg")
