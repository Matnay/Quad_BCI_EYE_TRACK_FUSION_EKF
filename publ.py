#!/usr/bin/env python
#A simulator to make a drone follow a certain trajectorty, suppose a square.
import rospy
from std_msgs.msg import Int32
from random import seed 
from random import randint
import time

def random_generate_noise():
    return randint(1,15)
def random_generate_signal():
    return randint(50,80)
def Talker():
     g=rospy.Publisher('gain', Int32, queue_size=10)
     l=rospy.Publisher('land', Int32, queue_size=10)
     f=rospy.Publisher('forward', Int32, queue_size=10)
     b=rospy.Publisher('backward', Int32, queue_size=10)
     le=rospy.Publisher('left', Int32, queue_size=10)
     rg=rospy.Publisher('right', Int32, queue_size=10)
     rospy.init_node('Simulator', anonymous=True)
     rate=rospy.Rate(10)
     while not rospy.is_shutdown():
            start = time.time()
            while time.time() < start + 5:
                no=random_generate_signal()
                g.publish(no)
                no=random_generate_noise()
                l.publish(no)
                no=random_generate_noise()
                f.publish(no)
                no=random_generate_noise()
                b.publish(no)
                no=random_generate_noise()
                le.publish(no)
                no=random_generate_noise()
                rg.publish(no)
                rospy.loginfo("Rise")
            start = time.time()
            while time.time() < start + 5:
                no=random_generate_noise()
                g.publish(no)
                no=random_generate_noise()
                l.publish(no)
                no=random_generate_signal()
                f.publish(no)
                no=random_generate_noise()
                b.publish(no)
                no=random_generate_noise()
                le.publish(no)
                no=random_generate_noise()
                rg.publish(no)
                rospy.loginfo("Forward")
            start = time.time()
            while time.time() < start + 5:
                no=random_generate_noise()
                g.publish(no)
                no=random_generate_noise()
                l.publish(no)
                no=random_generate_noise()
                f.publish(no)
                no=random_generate_noise()
                b.publish(no)
                no=random_generate_noise()
                le.publish(no)
                no=random_generate_signal()
                rg.publish(no)
                rospy.loginfo("Right")
            start = time.time()
            while time.time() < start + 5:
                no=random_generate_noise()
                g.publish(no)
                no=random_generate_noise()
                l.publish(no)
                no=random_generate_noise()
                f.publish(no)
                no=random_generate_signal()
                b.publish(no)
                no=random_generate_noise()
                le.publish(no)
                no=random_generate_noise()
                rg.publish(no)
                rospy.loginfo("Backwards")
            start = time.time()
            while time.time() < start + 5:
                no=random_generate_noise()
                g.publish(no)
                no=random_generate_noise()
                l.publish(no)
                no=random_generate_noise()
                f.publish(no)
                no=random_generate_signal()
                b.publish(no)
                no=random_generate_noise()
                le.publish(no)
                no=random_generate_noise()
                rg.publish(no)
                rospy.loginfo("Left")
            start = time.time()
            while time.time() < start + 5:
                no=random_generate_noise()
                g.publish(no)
                no=random_generate_signal()
                l.publish(no)
                no=random_generate_noise()
                f.publish(no)
                no=random_generate_noise()
                b.publish(no)
                no=random_generate_noise()
                le.publish(no)
                no=random_generate_noise()
                rg.publish(no)
                rospy.loginfo("Land")
if __name__ == '__main__':
    try:
        Talker()
    except rospy.ROSInterruptException:
        pass
