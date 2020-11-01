#!/usr/bin/env python
import rospy
from duckietown_msgs.msg import Twist2DStamped

def spin_test():
    pub = rospy.Publisher('/duck5/joy_mapper_node/car_cmd', Twist2DStamped, queue_size=10)
    rospy.init_node('spinner')
    rate = rospy.Rate(60)
    while not rospy.is_shutdown():
        data = Twist2DStamped()
        data.v = 0.1
        data.omega = -5
        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    try:
        spin_test()
    except rospy.ROSInterruptException:
        pass
