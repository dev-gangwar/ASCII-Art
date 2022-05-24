from PIL import Image,ImageDraw,ImageFont
lol=".;'/?><:}{|\!@#$%^&*()_+123456789asdfghjkl"
lol_width=10
lol_hieght=10
img=Image.open('/home/darik/Desktop/Dev/ASCII_Art/anime/10.jpg')
width,hieght=img.size
img=img.resize((int(width/lol_width),int(hieght/lol_hieght)),Image.NEAREST)
Width,Hieght=img.size
img=img.load()
ascii_img=Image.new('RGB',(width,hieght),(0,0,0))
fnt=ImageFont.truetype('/home/darik/Desktop/Dev/ASCII_Art/BRITANIC.ttf')
d=ImageDraw.Draw(ascii_img)
def getlol(value):
    return lol[int(value*(len(lol)/256))]

for i in range(Hieght):
    for j in range (Width):
        r,g,b=img[j,i]
        k=int((r+g+b)/3)
        d.text((j*lol_width,i*lol_hieght),getlol(k),font=fnt,fill=(r,g,b))
ascii_img.save('7.png')