#!/usr/bin/env python
import rospy
from apriltag_ros.msg import AprilTagDetectionArray
from duckietown_msgs.msg import BoolStamped

class Detection:
    def __init__(self):
        self.detected = False
        self.lastDetected = False
        self.pub = rospy.Publisher('/duck5/wheels_driver_node/emergency_stop', BoolStamped, queue_size=10)
        self.sub = rospy.Subscriber('/tag_detections', AprilTagDetectionArray, self.detectionCallback)
        rospy.spin()

    def detectionCallback(self, data):
        self.detected = False
        for detection in data.detections:
            for id_ in detection.id:
                if id_ == 2:
                    self.detected = True
        if self.detected == True and self.lastDetected == False:
            rospy.loginfo("detected tag id==2, stopping duckiebot")
            self.pubStop()
        elif self.detected == False and self.lastDetected == True:
            rospy.loginfo("restarting duckiebot")
            self.pubStop()
        self.lastDetected = self.detected
    
    def pubStop(self):
        rospy.loginfo("publishing emergency_stop")
        emstop = BoolStamped()
        emstop.data = True
        self.pub.publish(emstop)

if __name__ == '__main__':
    try:
        rospy.init_node('tag_detector')
        det = Detection()
        
    except rospy.ROSInterruptException:
        pass
