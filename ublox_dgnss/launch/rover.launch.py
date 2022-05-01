""" Launch ublox_dgnss_node publishing high precision Lon/Lat messages"""
import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.actions import LoadComposableNodes
from launch_ros.actions import Node
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
  """Generate launch description for ublox_dgnss components."""
  params = [{'CFG_USBOUTPROT_NMEA': False},
            {'CFG_MSGOUT_UBX_NAV_HPPOSLLH_USB': 1},
            {'CFG_MSGOUT_UBX_NAV_STATUS_USB': 5}]
            # ANY CONFIG APPLIED ABOVE IS TEMPORARY. 
            # CONFIG STORED IN FLASH IS STILL USED BY UBLOX CHIP.
            #{'CFG_RATE_MEAS': 100},
            #{'CFG_RATE_NAV': 1},
            #{'CFG-USBINPROT-RTCM3X': 1}]

  container1 = ComposableNodeContainer(
    node_name='gps_rover_container',
    node_namespace='',
    package='rclcpp_components',
    node_executable='component_container',
    composable_node_descriptions=[
      ComposableNode(
        package='ublox_dgnss_node',
        node_plugin='ublox_dgnss::UbloxDGNSSNode',
        node_name='gps_rover',
        parameters=params
      )
    ]
  )

  return launch.LaunchDescription([container1])
