#!/usr/bin/env python3
# *-* coding: utf-8 *-*

import sys
import math
import cmath

def scalProd(c1, c2):
    return c1.real*c2.real + c1.imag*c2.imag
def orth(v):
    return complex(v.imag, -v.real)/abs(v)
class Points():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.angle = 0

class Pods():
    def __init__(self, id, x, y, vx, vy, angle, nextCheckPointId):
        self.id = id
        self.x = x
        self.y = y
        self.v = complex(vx, vy)
        self.accel = complex(0,0)
        self.angle = angle
        self.nextCheckPointId = nextCheckPointId
    def __str__(self):
        return "Pod #" +str(self.id)+ " (chkpt #" + str(self.nextCheckPointId) +"), x=" + str(self.x)+", y="+str(self.y)+", angle="+str(self.angle)
    def countTimeToGo(self, target):
        i = 1
        me = self
        while(i<20):
            me = me.nextpos()
            if me.distanceTo(target) < 600:
                return i
            else:
                #print("ToGo compute #" + str(i) + " not yet at " + str(me.distanceTo(target)) + "since me=" + str(me), file = sys.stderr)
                i+=1
        return 20
    def countTimeToTurn(self, pos, target):
        vector = complex(target[0]-pos[0], target[1]-pos[1])
        #print("target = " + str(target) + " and pos = " + str(pos), file=sys.stderr)
        cap = cmath.phase(vector)*180/math.pi
        #print("Computed Cap = " + str(cap) + " and angle = " + str(self.angle), file=sys.stderr)
        diffcap = abs((cap - self.angle)) % 360
        diffcap = min(diffcap, 360-diffcap)
        #print("Computed DiffCap = " + str(diffcap), file=sys.stderr)
        return int(diffcap/18)
    def nextpos(self):
        return Pods(self.id, self.x + self.v.real + self.accel.real, self.y + self.v.imag + self.accel.imag, (self.v.real+self.accel.real)*0.85, (self.v.imag+self.accel.imag)*0.85, self.angle, self.nextCheckPointId)
    def distanceTo(self, otherpod):
        vector = complex(otherpod.x - self.x, otherpod.y - self.y)
        return abs(vector)
    def cap(self, otherpod):
        vector = complex(otherpod.x - self.x, otherpod.y - self.y)
        return cmath.phase(vector)*180/math.pi
    def diffcap(self, otherpod):
        diff = abs(self.angle - self.cap(otherpod)) % 360
        print("Computed cap " + str(self.cap(otherpod)), file=sys.stderr)
        return min(diff, 360-diff)
    def collide(self, otherpod):
        me = self.nextpos()
        him = otherpod
        diffcap = him.diffcap(me)
        print("Danger from " + str(him.id) + " with diffcap " + str(diffcap), file=sys.stderr)
        if diffcap<18:
            him.angle = him.cap(me)
            him.accel = cmath.rect(200, him.angle*math.pi/180)
            print(str(him.id) + " could try to hit me as diffcap is " + str(diffcap), file=sys.stderr)
        else:
            him.accel = cmath.rect(200, him.angle*math.pi/180)
        him = him.nextpos()
        if me.distanceTo(him) < 800:
            print("IT WILL HIT ME", file=sys.stderr)
            print("Next distance " + str(me.distanceTo(him)) + "since him=" + str(him) + "and me=" + str(me), file=sys.stderr)
            return complex(me.x-him.x, me.y-him.y)
        else:
            print("Next distance " + str(me.distanceTo(him)) + "since him=" + str(him) + "and me=" + str(me), file=sys.stderr)
        
        return False

laps = int(input())
checkpoint_count = int(input())
checkpoints = []
for i in range(checkpoint_count):
    checkpoint_x, checkpoint_y = [int(j) for j in input().split()]
    checkpoints.append((checkpoint_x, checkpoint_y))

# game loop
turn = 0
while True:
    mypods = []
    theirpods = []
    for i in range(2):
        x, y, vx, vy, angle, nextCheckPointId = [int(j) for j in input().split()]
        mypods.append(Pods(i, x, y, vx, vy, angle, nextCheckPointId))
    for i in range(2):
        x, y, vx, vy, angle, nextCheckPointId = [int(j) for j in input().split()]
        theirpods.append(Pods(i, x, y, vx, vy, angle, nextCheckPointId))
        print("Bad pod " + str(theirpods[i]), file=sys.stderr)
    for i in range(2):
        print("=== POD #" + str(i) + " ===", file=sys.stderr)
        if False and turn < 4:
            print(str(mypods[(i+1)%2].x) + " " + str(mypods[(i+1)%2].y) + " 0")
        elif False and True:
            speed = 200
            if i == 1 and turn < 8:
                speed = "0"
            if i ==0 and turn == 8:
                speed = "SHIELD"
            print(str(mypods[(i+1)%2].x) + " " + str(mypods[(i+1)%2].y) + " " + str(speed))
        else:
            thispod = mypods[i]
            shield = False
            msg = ""
            nextcheckpoint = checkpoints[thispod.nextCheckPointId]
            nextnextcheckpoint = checkpoints[(thispod.nextCheckPointId+1) % len(checkpoints)]
            timeToTurn = thispod.countTimeToTurn(nextcheckpoint, nextnextcheckpoint)
            timeToGo = thispod.countTimeToGo(Points(nextcheckpoint[0], nextcheckpoint[1]))
            print("ToTurn : "+str(timeToTurn)+",ToGo : "+str(timeToGo), file=sys.stderr)
            vector = complex(nextcheckpoint[0]-thispod.x, nextcheckpoint[1]-thispod.y)
            distance = abs(vector)
            
            if False and i==1 and turn==2:
                print(str(nextcheckpoint[0]) + " " + str(nextcheckpoint[1]) + " SHIELD")
            elif timeToTurn > timeToGo:
                actualtarget = nextnextcheckpoint
                thrust = 0
                print("Preparing next checkpoint : " + str(nextnextcheckpoint), file=sys.stderr)
            else:
                #Let's compute destination:
                decal = orth(vector)*1200
                s = scalProd(decal, thispod.v)
                if s>0:
                    decal = -decal
                if abs(s) < 30000:
                    actualtarget = nextcheckpoint
                else:
                    actualtarget = (nextcheckpoint[0]+decal.real, nextcheckpoint[1]+decal.imag)
                #Let's compute thrust:
                thrust = 200#min(200, int(distance/10))
                cap = cmath.phase(vector)*180/math.pi
                diffcap = abs((cap - thispod.angle))
                diffcap = min(diffcap, 360-diffcap)
                thispod.accel = vector/abs(vector)*thrust
                if turn > 1:
                    if diffcap > 18:
                        # We are not aligned ! Maybe we need to turn with 0 thrust.
                        if abs(vector)/abs(thispod.v) > 4*(diffcap/18):
                            #we are far enough, let's get outta here
                            msg += "Yolo"
                        else:
                            print("Not aligned ! Diffcap = " + str(diffcap) + " as cap=" + str(cap) + " and angle=" + str(thispod.angle), file=sys.stderr)
                            thrust = 0
                            if diffcap > 4*18:
                                shield = True
            #Let's handle collisions
            if turn>1:
                for j in range(2):
                    vc = thispod.collide(theirpods[j])
                    if vc:
                        vc = vc/abs(vc)
                        alienspeed = vc*scalProd(theirpods[j].v+theirpods[j].accel, vc)
                        if (abs(alienspeed)>400 and
                            (scalProd(alienspeed, vector)<0 or
                            abs(scalProd(alienspeed/abs(alienspeed), orth(vector)))>0.3)):
                            print("Shield OK with " + str(abs(thispod.v)+abs(alienspeed)) + " and " +str(alienspeed) + " so " + str((scalProd(alienspeed, vector))) + " or " + str(scalProd(alienspeed/abs(alienspeed), orth(vector))), file=sys.stderr)
                            thrust = 0
                            thispod.accel = complex(0,0)
                            if(thispod.collide(theirpods[j])):
                                shield = True
                                msg = "DANGER"
                            else:
                                shield = True
                                msg = "Ninja"
                        else:
                            print("Shield not worth it with " + str(abs(thispod.v)+abs(alienspeed)) + " and " +str(alienspeed) + " so " + str((scalProd(alienspeed, vector))) + " or " + str(scalProd(alienspeed/abs(alienspeed), orth(vector))), file=sys.stderr)
                            msg+="xD"
                
            if shield:
                thrust = "SHIELD"
            if len(msg) > 0:
                msg = " " + msg
            print(str(int(actualtarget[0])) + " " + str(int(actualtarget[1])) + " " + str(thrust) + msg)
    turn += 1
