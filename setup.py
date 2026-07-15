from setuptools import find_packages, setup


package_name = "runtime_bootstrap"


setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/runtime_bootstrap"]),
        (f"share/{package_name}", ["package.xml"]),
        (f"share/{package_name}/launch", ["launch/runtime_bootstrap.launch.py"]),
        (f"share/{package_name}/config", ["config/runtime_bootstrap.yaml"]),
        (f"share/{package_name}/docs", ["docs/system-overview.md", "docs/development.md"]),
    ],
    install_requires=[],
    zip_safe=True,
    maintainer="Runtime Bootstrap Maintainers",
    maintainer_email="maintainers@example.com",
    description="Workspace-oriented bootstrap helper for robotics and ROS 2 development",
    license="MIT",
    entry_points={
        "console_scripts": [
            "check-bootstrap = runtime_bootstrap.cli:check_bootstrap_main",
        ],
    },
)
