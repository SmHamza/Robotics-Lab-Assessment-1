import pyowm
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'weather/requests',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        
    def listener_callback(self, msg):
        owm = pyowm.OWM('6ae8bcd8994718e41f74564ec85170ef')
        mng = owm.weather_manager()
        obs = mng.weather_at_place(msg.data).weather.temperature(unit='celsius')
        topic = 'weather/%s' % msg.data
        if obs is not None:
            self.publisher_ = self.create_publisher(String, topic, 10)
            self.get_logger().info('Temperature: "%s"' % obs)
        


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
