from tank import Tank
t1=Tank(x=0,y=0)
t2=Tank(x=100,y=100,model="13 Армата",ammo=80)
print(f"создано танков:{Tank.count}")
t1.backward()
t1.backward()
t1.right()
t1.fire()
print(t1)