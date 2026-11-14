"""Render an original signal-field illustration. No measured data is depicted."""
from math import cos, exp, pi, sin
import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

W, H = 1500, 1080
random.seed(19)
base = Image.new('RGB', (W,H), '#091f27')
draw = ImageDraw.Draw(base)
for y in range(H):
    k = sin(y/H*pi)
    draw.line((0,y,W,y),fill=(int(9+2*k),int(29+8*k),int(36+9*k)))
for i in range(380):
    x,y = random.randrange(W),random.randrange(H)
    v=random.randrange(38,90)
    draw.point((x,y),fill=(v-8,v+7,v+10))
for x in range(50,W,110):
    for y in range(65,H,110):
        draw.line((x-3,y,x+3,y),fill='#25424a')
        draw.line((x,y-3,x,y+3),fill='#25424a')
def pos(t,s):
    # Perspective folds move through the field at different phases.
    x= -180 + 1660*t + 215*s
    y= 680 - 210*t + s*290 - 225*exp(-((t-.58-.19*s)/.14)**2) + 94*sin(2*pi*(1.82*t+.54*s)) + 57*sin(2*pi*(.81*t-1.47*s))
    return x,y
layer=Image.new('RGBA',(W,H)); pen=ImageDraw.Draw(layer)
for j in range(135):
    s=j/134
    pts=[pos(i/500,s) for i in range(501)]
    a=.5+.5*cos(2*pi*(s-.1))
    col=(int(80+72*a),int(181+58*a),int(178+55*a),int(85+130*a))
    pen.line(pts, fill=col,width=2 if j%5==0 else 1)
for i in range(0,500,7):
    pen.line([pos(i/500,j/134) for j in range(135)], fill=(110,182,184,57),width=1)
base=base.convert('RGBA')
base=Image.alpha_composite(base,layer.filter(ImageFilter.GaussianBlur(5)))
base=Image.alpha_composite(base,layer)
pen=ImageDraw.Draw(base)
pts=[pos(i/500,.58) for i in range(501)]
pen.line(pts,fill='#f3b882',width=3)
x,y=pos(.66,.58)
for r in [15,8]:
    pen.ellipse((x-r,y-r,x+r,y+r),outline='#ffd099',width=2)
pen.ellipse((x-3,y-3,x+3,y+3),fill='#ffce9c')
base.convert('RGB').save(Path(__file__).resolve().parents[1]/'assets/signal-field.webp',quality=93,method=6)
