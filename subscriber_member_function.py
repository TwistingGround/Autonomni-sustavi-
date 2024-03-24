import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class ListenerAndPublisher(Node):

    def __init__(self):
        super().__init__('listener_and_publisher')

        #creating listener
        self.subscription = self.create_subscription(
            Int32,
            'broj',
            self.listener_callback,
            10)

        #creating publisher
        self.publisher = self.create_publisher(
            Int32,
            'kvadrat_broja',
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%d"' % msg.data)

        squared_number = msg.data ** 2

        squared_msg = Int32()
        squared_msg.data = squared_number
        self.publisher.publish(squared_msg)
        self.get_logger().info('Publishing: %d' %squared_number)


def main(args=None):
    rclpy.init(args=args)

    listener_and_publisher = ListenerAndPublisher()

    rclpy.spin(listener_and_publisher)

    listener_and_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
