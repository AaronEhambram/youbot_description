from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    ld = LaunchDescription()

    urdf_path = FindPackageShare('youbot_description')
    default_model_path = PathJoinSubstitution([urdf_path, 'robots', 'youbot.urdf.xacro'])

    # This parameter has changed its meaning slightly from previous versions
    ld.add_action(DeclareLaunchArgument(name='model', default_value = default_model_path,
                                        description='Path to robot urdf file relative to urdf_tutorial package'))

    ld.add_action(IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare('urdf_launch'), 'launch', 'description.launch.py']),
        launch_arguments={
            'urdf_package': 'youbot_description',
            'urdf_package_path': LaunchConfiguration('model')
            }.items()
    ))

    return ld


