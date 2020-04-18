#!/usr/bin/env python
import rospy
import sensor_msgs.point_cloud2 as pc2
import random
from sensor_msgs.msg import PointCloud2, PointField
from std_msgs.msg import Header

rospy.init_node('my_pc2_publisher')

topic_name = '/my_pc2'
frame_name = 'base_link'

pc2_header = Header()
pc2_header.frame_id = frame_name

pc2_fields = [PointField('x', 0, PointField.FLOAT32, 1),
             PointField('y', 4, PointField.FLOAT32, 1),
             PointField('z', 8, PointField.FLOAT32, 1),
             PointField('intensity', 12, PointField.FLOAT32, 1)]

pc2_pub = rospy.Publisher(topic_name, PointCloud2, queue_size=1)

z = 0.0
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    x = random.random()
    y = random.random()
    p1 = [x, 0., z, 1.]
    p2 = [x, y, z, 0.5]
    z += 0.1
    points = [p1, p2]
    pc2_header.stamp = rospy.Time.now()
    pc2_msg = pc2.create_cloud(pc2_header, pc2_fields, points)
    pc2_pub.publish(pc2_msg)
    rate.sleep()
