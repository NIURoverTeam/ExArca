from setuptools import setup
from glob import glob

package_name = 'ad_boxtra'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        #('share/' + package_name, ['launch/launch_drive_control.py']),
        ('share/' + package_name, glob('launch/*.py')), # include all launch files
        ('share/' + package_name, glob('resource/*.urdf')), # include all webots-related resource files
        ('share/' + package_name + '/webots_simulation/worlds',    # include desired webots worlds
            ['adboxtra_2022_simplified.wbt']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='luckierdodge',
    maintainer_email='ryandlewis.rl@gmail.com',
    description="ROS 2 Package to drive the NIU Mars Rover Team's Ad Boxtra platform.",
    license='MIT License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle_ad_boxtra = ad_boxtra.turtle_ad_boxtra:main',
            'conversationalist = ad_boxtra.conversationalist:main',
            'drive_control_serial = ad_boxtra.drive_control_serial:main',
            'my_robot_driver = ad_boxtra.my_robot_driver:main',
        ],
    },
)
