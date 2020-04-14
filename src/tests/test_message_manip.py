#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Transform
from geometry_msgs.msg import Vector3
from fiducial_msgs.msg import FiducialTransform

from geometry_representation import MessageTransformer

rospy.init_node('test_message_manip_package', anonymous=True)

if __name__ == "__main__":
    pose = Pose(Point(1, 2, 3), Quaternion(4, 5, 6, 7))
    transform = Transform(Vector3(1, 2, 3), Quaternion(4, 5, 6, 7))

    if not MessageTransformer.pose_equals(pose, pose):
        rospy.loginfo("error with pose equality function")

    pose_found = MessageTransformer.pose_from_transform(transform)
    if not MessageTransformer.pose_equals(pose, pose_found):
        rospy.loginfo("error when parsing transform into pose")
        rospy.loginfo("actual pose is : ")
        rospy.loginfo(pose)
        rospy.loginfo("pose found is : ")
        rospy.loginfo(MessageTransformer.pose_from_transform(transform))

    fiducial = FiducialTransform(1, transform, 0, 0, 0)

    results = MessageTransformer.fiducial_analyser(fiducial)
    if not (results[0] == 1 and MessageTransformer.pose_equals(pose, results[1])):
        rospy.loginfo("error when analysing fiducial")