import rclpy
import datetime
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.subscription = self.create_subscription(
            String,
            'clock/setalarm',
            self.listener_callback,10)
        self.subscription  # prevent unused variable warning
        self.publisher_ = self.create_publisher(String, 'clock/alarm', 10)
        timer_period =  1 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
    def listener_callback(self, msg):
        self.partition = str(msg.data)
        self.time = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second)
        if self.partition > self.time:
            print("Alarm Time:" + self.partition + " Current Time:" + self.time)
        if self.partition == self.time:
            print("Sending Alarm Notification")
            msg = String()
            msg.data = 'Alarm On. Wake up!'
            self.publisher_.publish(msg)
            # self.get_logger().info('Publishing: "%s"' % msg.data)

    def timer_callback(self):
        self.time = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second)
        
def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
