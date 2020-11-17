#!/usr/bin/env python
import rospy
from apriltag_ros.msg import AprilTagDetectionArray
from duckietown_msgs.msg import BoolStamped

class Detection:
    def __init__(self):
        self.detected = False
        self.pub = rospy.Publisher('/duck5/wheels_driver_node/emergency_stop', BoolStamped, queue_size=10)
        self.sub = rospy.Subscriber('/tag_detections', AprilTagDetectionArray, self.detectionCallback)
        self.pubStop()
        rospy.spin()

    def detectionCallback(self, data):
        for detection in data.detections:
            for id_ in detection.id:
                if id_ == 2:
                    rospy.loginfo("detected tag id==2, stopping duckiebot")
                    self.detected = True
                    return
        self.detected = False
    
    def pubStop(self):
        rate = rospy.Rate(60)
        while not rospy.is_shutdown():
            if self.detected == True:
                rospy.loginfo("publishing emergency_stop")
                emstop = BoolStamped()
                emstop.data = True
                self.pub.publish(emstop)
                rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('tag_detector')
        det = Detection()
        
    except rospy.ROSInterruptException:
        pass
