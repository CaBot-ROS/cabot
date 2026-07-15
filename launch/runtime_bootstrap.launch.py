from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration


def generate_launch_description() -> LaunchDescription:
    record_path = LaunchConfiguration("bootstrap_record")

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "bootstrap_record",
                default_value="artifacts/bootstrap.json",
                description="Repository-local bootstrap record path.",
            ),
            LogInfo(msg=["runtime_bootstrap launch active, record path: ", record_path]),
        ]
    )
