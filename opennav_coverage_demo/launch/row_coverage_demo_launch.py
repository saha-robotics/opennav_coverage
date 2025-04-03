# Copyright (c) 2023 Open Navigation LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')
    coverage_demo_dir = get_package_share_directory('opennav_coverage_demo')

    param_file_path = os.path.join(coverage_demo_dir, 'demo_params.yaml')
    namespace_cmd = DeclareLaunchArgument(
        'namespace',
        default_value=os.getenv("SMR_PREFIX", "none"),
        description="Robot namespace prefix",
    )
    namespace = LaunchConfiguration("namespace")

    # start navigation
    bringup_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(coverage_demo_dir, 'row_bringup_launch.py')),
        launch_arguments={'params_file': param_file_path,
                        'namespace': namespace}.items())

    # start the demo task
    demo_cmd = Node(
        package='opennav_coverage_demo',
        executable='demo_row_coverage',
        namespace=namespace,
        emulate_tty=True,
        output='screen')

    ld = LaunchDescription()
    ld.add_action(namespace_cmd)
    ld.add_action(bringup_cmd)
    ld.add_action(demo_cmd)
    return ld
