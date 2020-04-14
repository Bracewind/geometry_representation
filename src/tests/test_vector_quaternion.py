#!/usr/bin/env python

import rospy

import numpy as np
import quaternion

from geometry_representation import VectorQuaternion


def test_vector():
    a = VectorQuaternion(np.quaternion(0, 1, 2, 3))
    b = VectorQuaternion(np.quaternion(0, 2, 1, 3))

    if a.dot(b) != 13:
        rospy.loginfo("bug with dot product")

    if (a-b) != VectorQuaternion(np.quaternion(0, -1, 1, 0)):
        rospy.loginfo("bug with subtraction")


if __name__=="__main__":
    test_vector()