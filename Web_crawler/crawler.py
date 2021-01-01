from urllib.request import urlopen

baseUrl = "https://map0.daumcdn.net/"
midadrr = ["map_skyview", "map_2d/2012tlq"]

#positions
start_y = 437
start_x = 188
finish_y = 521
finish_x = 244

n=1
for i in range(start_y, finish_y + 1):
    for j in range(start_x, finish_x + 1):
        for k in midadrr:
            url = baseUrl + k + '/' + 'L5' +'/' + str(i) + '/' + str(j) + (".jpg" if k == "map_skyview" else ".png")
            print(url)
            with urlopen(url) as f:
                with open( './images/L5/' + ("sky" if k == "map_skyview" else "map") + str(n) +'.png', 'wb') as h:
                    img = f.read()
                    h.write(img)
        n = n + 1




