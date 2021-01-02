from urllib.request import urlopen
import ssl

baseUrl = "https://map0.daumcdn.net/"
midadrr = ["map_skyview", "map_2d/2012tlq"]

#positions
start_y = 2513
start_x = 2904
finish_y = 2560
finish_x = 2936

n=0
for i in range(start_y, finish_y + 1):
    for j in range(start_x, finish_x + 1):
        for k in midadrr:
            url = baseUrl + k + '/' + 'L2' +'/' + str(i) + '/' + str(j) + (".jpg" if k == "map_skyview" else ".png")
            print(url)
            with urlopen(url) as f:
                with open( './images/L2/' + ("sky" if k == "map_skyview" else "map") + str(n) +'.png', 'wb') as h:
                    img = f.read()
                    h.write(img)
        n = n + 1