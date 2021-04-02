import rclpy
import datetime
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.hour = int(input("Enter Hour: "))
        self.min = int(input("Enter Min: "))
        self.sec = int(input("Enter Second: "))
        self.alarm = str(self.hour) + ":" + str(self.min) + ":" + str(self.sec)
        print(self.alarm)
        self.publisher_ = self.create_publisher(String, 'clock/setalarm', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.subscription = self.create_subscription(
            String,
            'clock/alarm',
            self.listener_callback,10)
        self.subscription  # prevent unused variable warning

    def timer_callback(self):
        msg = String()
        msg.data = self.alarm
        self.publisher_.publish(msg)
        # self.get_logger().info('Publishing: "%s"' % msg.data)
    def listener_callback(self, msg):
        # self.partition = str(msg).split(":")[3]
        # if self.partition == "0')":
            self.get_logger().info(msg.data)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
