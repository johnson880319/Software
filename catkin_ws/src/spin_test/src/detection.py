#!/usr/bin/env python
import rospy
from apriltag_ros.msg import AprilTagDetectionArray
from duckietown_msgs import BoolStamped

class detection:
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
        while self.detected == True:
            emstop = BoolStamped()
            emstop.data = True
            pub.publish(emstop)

if __name__ == '__main__':
    try:
        rospy.init_node('tag_detector')
        spin_test()
        
    except rospy.ROSInterruptException:
        pass
