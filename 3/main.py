from hitbox import Hitbox

#hb1=Hitbox(0,100,100,100)
#hb2=Hitbox(150,100,100,100)

#print(f"верхняя граница hb1: {hb1.top}, верхняя граница hb2: {hb2.top}")
#print(f"нижняя граница hb1: {hb1.bottom}, нижняя граница hb2: {hb2.bottom}")
#print(f"левая граница hb1: {hb1.left}, левая граница hb2: {hb2.left}")
#print(f"равая граница hb1: {hb1.right}, правая граница hb2: {hb2.right}")


#intersection=hb1.intersects(hb2)
#print(intersection)
from tank import Tank
from tkinter import*

def key_press(event):
    print(f'ажата клавиша {event.keysym}, код {event.keycode}')

KEY_W=87
KEY_S=83
KEY_A=65
KEY_D=68

def check_collision():
    if player.inersects(enemy):
        print("Такни столкнулись")

def key_press(event):
    if event.keycode == KEY_W:
        player.forvard()
    if event.keycode == KEY_S:
        player.backward()
    if event.keycode == KEY_A:
        player.left()
    if event.keycode == KEY_D:
        player.right()
    check_collision()

w=Tk()
w.title('Танки на минималках 2.0')
canv=Canvas(w,width=800,height=600,bg='alice blue')
canv.pack()
player=Tank(canvas=canv,x=100,y=50,ammo=100)

enemy=Tank(canvas = canv, x = 300, y=300, ammo = 100)

w.bind('<KeyPress>', key_press)
w.mainloop()
